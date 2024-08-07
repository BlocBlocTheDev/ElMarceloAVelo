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

found_event = Event()

def process_station_wrapper(AllStationsID):
    """Wrapper pour la fonction process_station."""
    try:
        return process_station(AllStationsID), AllStationsID
    except Exception as e:
        print(f"Une erreur est survenue pour la station {AllStationsID}: {e}")
        return None, AllStationsID

with ThreadPoolExecutor(max_workers=4) as executor:
    # Soumettre toutes les tâches et créer une map future -> station_id
    future_to_station = {executor.submit(process_station_wrapper, station_id): station_id for station_id in AllStationsID}

    for future in as_completed(future_to_station):
        # On vérifie si le vélo a été trouvé via l'événement
        if found_event.is_set():
            # Si l'événement est déjà activé, on ignore les autres résultats
            continue

        try:
            result, station_id = future.result()

            if result:
                NomStation, value, velo, places, place, bikes_data = result
                # Vérifier si le vélo recherché est dans les données
                if choosedbike in bikes_data:
                    lignearray = bikes_data[choosedbike]
                    IDOfBike = lignearray.get('IDBike')
                    BATOfBike = lignearray.get('BATBike')
                    KMOfBike = lignearray.get('KMBike')
                    blokedbike = lignearray.get('Bloked')

                    if blokedbike == True:
                        statutbike = "est bloqué par un autre vélo"
                    elif blokedbike == False:
                        statutbike = "n'est pas bloqué par un autre vélo"
                    else:
                        statutbike = "son statut n'est pas disponible"

                    print("\n")
                    print(f"Vélo trouvé !")
                    print(f"Le vélo N°{choosedbike} est à la station {NomStation}, possède {BATOfBike} de batterie (Soit {KMOfBike}) et {statutbike}")
                    
                    # Activer l'événement pour signaler que le vélo a été trouvé
                    found_event.set()
                    break  # Sortir de la boucle for

        except Exception as e:
            # Gérer les exceptions potentielles
            print(f"Une erreur s'est produite: {e}")

    # Annuler les futures restantes (si possible)
    for future in future_to_station:
        future.cancel()

if not found_event.is_set():
    print(f"Le vélo N°{choosedbike} n'a pas été trouvé dans aucune station.")

print("\n" * 2)
print("Fin de recherche")
print("El Marcelo A Velo - BlocBlocTheBloc Code")