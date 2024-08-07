query = "SELECT ID FROM LIST_STATION ORDER BY RAND()"

cursor.execute(query)

result = cursor.fetchall()

AllStationsID = [row[0] for row in result]

