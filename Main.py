with open('Deps/imports.py', 'r') as file:
    code = file.read()
    exec(code)

with open('Deps/webdriver.py', 'r') as file:
    code = file.read()
    exec(code)

with open('Deps/msqlconfig.py', 'r') as file:
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
tatol = 0

print("El Marcelo A Velo - BlocBlocTheBloc Code")
print("Rapport complet des stations et vélos associées avec import dans la Base")
print("\n")
print("\n")

with ThreadPoolExecutor(max_workers=4) as executor:
    future_to_station = {executor.submit(process_station, AllStationsID): AllStationsID for AllStationsID in AllStationsID}

    for future in as_completed(future_to_station):
        AllStationsID = future_to_station[future]
        try:
            NomStation, value, velo, places, place, bikes_data = future.result()
            if NomStation:
                with open('Defs/update.py', 'r') as file:
                    code = file.read()
                    exec(code)

                with open('Defs/tracking_station.py', 'r') as file:
                    code = file.read()
                    exec(code)

                if bikes_data != {}:
                    print(f"    {NomStation} possède {value} {velo} et {place} {places} libres dont :")
                    for i, (id_bike, data) in enumerate(bikes_data.items(), start=1):
                        bat_bike = data.get('BATBike', 'Inconnu')
                        km_bike = data.get('KMBike', 'Inconnu')
                        blokedbike = data.get('Bloked', 'Inconnu')
                        if blokedbike == True:
                            statutbike = "est bloqué par un autre vélo"
                        elif blokedbike == False:
                            statutbike = "n'est pas bloqué par un autre vélo"
                        else:
                            statutbike = "son statut n'est pas disponible"
                        print(f"        Vélo N°{id_bike} à {bat_bike} de batterie, peut faire {km_bike} et {statutbike}")
                else:
                    print(f"    {NomStation} possède {value} {velo} et {place} {places} libres")
                total += value
                tatol += place
                print("\n")

        except Exception as e:
            print(f"Une erreur est survenue pour la station {AllStationsID}: {e}")

# Afficher le total des vélos à la fin
print(f"Nombre de vélo en stations : {total} vélos")
print("\n")
print(f"Nombre total de places libres en stations : {tatol} places")
print("\n")
print("\n")
print("Fin de Rapport")
print("Base de données mise à jour")
print("El Marcelo A Velo - BlocBlocTheBloc Code")