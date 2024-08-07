with open('Deps/imports.py', 'r') as file:
    code = file.read()
    exec(code)

with open('Deps/webdriver.py', 'r') as file:
    code = file.read()
    exec(code)

with open('Defs/accept_cookies.py', 'r') as file:
    code = file.read()
    exec(code)

with open('Defs/get_station_data.py', 'r') as file:
    code = file.read()
    exec(code)

with open('Defs/AllStations.py', 'r') as file:
    code = file.read()
    exec(code)

with open('Defs/process_station.py', 'r') as file:
    code = file.read()
    exec(code)

total = 0

DateNow = datetime.now()

print("El Marcelo A Velo")
print("Rapport des données de Vélo et Stations")
print("Date de début :", DateNow)

with ThreadPoolExecutor(max_workers=4) as executor:
    future_to_station = {executor.submit(process_station, AllStationsID): AllStationsID for AllStationsID in AllStationsID}

    for future in as_completed(future_to_station):
        AllStationsID = future_to_station[future]
        try:
            NomStation, value, velo, places, place, bikes_data = future.result()
            if NomStation:
                if bikes_data != {}:
                    print(f"    {NomStation} possède {value} {velo} dont :")
                    for i, (id_bike, data) in enumerate(bikes_data.items(), start=1):
                        bat_bike = data.get('BATBike', 'Inconnu')
                        km_bike = data.get('KMBike', 'Inconnu')
                        print(f"        Vélo N°{id_bike} à {bat_bike} de batterie et peut faire {km_bike}")
                else:
                    print(f"    {NomStation} possède {value} {velo}")
                total += value
                print("\n")
        except Exception as e:
            print(f"Une erreur est survenue pour la station {AllStationsID}: {e}")

# Afficher le total des vélos à la fin
print(f"\nTotal des vélos en station : {total}")

print("Fin de Rapport")
DateNow = datetime.now()
print("Date de fin :", DateNow)