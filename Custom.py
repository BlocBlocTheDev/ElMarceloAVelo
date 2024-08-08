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

print("El Marcelo A Velo - BlocBlocTheBloc Code")
print("Recherche de vélo")
print("\n" * 2)

choosedbike = input("Numéro du vélo recherché : ")  # Récupère comme chaîne de caractères
print(f"Recherche du vélo N°{choosedbike} en cours...")

found = False  # Drapeau pour indiquer si le vélo a été trouvé

def process_station_wrapper(AllStationsID):
    """Wrapper pour la fonction process_station."""
    try:
        return process_station(AllStationsID), AllStationsID
    except Exception as e:
        print(f"Une erreur est survenue pour la station {AllStationsID}: {e}")
        return None, AllStationsID

with ThreadPoolExecutor(max_workers=4) as executor:
    future_to_station = {executor.submit(process_station_wrapper, AllStationsID): AllStationsID for AllStationsID in AllStationsID}

    for future in as_completed(future_to_station):
        result, AllStationsID = future.result()

        # Mettez votre code ICI !
            

print("\n" * 2)
print("Fin de Script")
print("El Marcelo A Velo - BlocBlocTheBloc Code")