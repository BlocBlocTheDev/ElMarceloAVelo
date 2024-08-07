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

bikes_data = {}

with ThreadPoolExecutor(max_workers=4) as executor:
    future_to_station = {executor.submit(process_station, AllStationsID): AllStationsID for AllStationsID in AllStationsID}

    for future in as_completed(future_to_station):
        AllStationsID = future_to_station[future]
        try:
            NomStation, value, velo, places, place, bikes_data = future.result()
            if NomStation:
                print(f"{NomStation} possède {place} {places}")
                total += place
        except Exception as e:
            print(f"Une erreur est survenue pour la station {AllStationsID}: {e}")

# Afficher le total des vélos à la fin
print(f"\nTotal d'emplacements libres en station : {total}")