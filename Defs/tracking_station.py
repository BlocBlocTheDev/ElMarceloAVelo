#print(f"Ajout des données de Tracking de {NomStation}")
                
try:
    DateByPython = datetime.now()
    Seconde = int(DateByPython.second)
    Heure = int(DateByPython.hour)
    Minute = int(DateByPython.minute)
    An = int(DateByPython.year)
    Mois = int(DateByPython.month)
    Jour = int(DateByPython.day)
    str(AllStationsID)
    str(NomStation) 
    SQL = f"""INSERT INTO `TRACK_STATION_{AllStationsID}`(
            `Velo`,
            `Place`,
            `Heure`,
            `Minute`,
            `Seconde`,
            `Jour`,
            `Mois`,
            `An`
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(SQL, (value, place, Heure, Minute, Seconde, Jour, Mois, An))
    conn.commit()
    #print(f"Donénes de Tracking de {NomStation} ajoutées avec succès")
except Exception as e:
    print(f"L'ajout des données de Tracking de {NomStation} a rencontré un problème : {e}")
    conn.rollback()

print("\n")