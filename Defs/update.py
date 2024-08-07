#print(f"Ajout de la Station {NomStation}")
DateByPython = datetime.now()
Seconde = int(DateByPython.second)
Heure = int(DateByPython.hour)
Minute = int(DateByPython.minute)
An = int(DateByPython.year)
Mois = int(DateByPython.month)
Jour = int(DateByPython.day)
str(AllStationsID)
str(NomStation)

try:
    SQL = (f'''
        UPDATE LIST_STATION SET
            NomStation = %s,
            Velo = %s,
            Places = %s,
            Heure = %s,
            Minute = %s,
            Seconde = %s,
            An = %s,
            Mois = %s,
            Jour = %s
        WHERE ID = %s;

    ''')
    values = (NomStation, value, place, Heure, Minute, Seconde, An, Mois, Jour, AllStationsID)
    cursor.execute(SQL, values)
    conn.commit()
    #print(f"{NomStation} Ajouté à la base")

except Exception as e:
    print(f"Impossible d'ajouter la Station {NomStation} : {e}")
    conn.rollback()

print("\n")