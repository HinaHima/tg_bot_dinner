#importing the database
import sqlite3

#connecting to the db
db = sqlite3.connect("next.db")
#creating a cursor
cursor = db.cursor()

#cursor.execute("""CREATE TABLE IF NOT EXISTS next(
    #date TEXT NOT NULL,
    #location TEXT NOT NULL,
    #places TEXT NOT NULL,
    #cost TEXT NOT NULL,
    #film TEXT NOT NULL
#)""")

#info = ["12.12.12", "BBB", "25 свободных", "3.500", "Секрет"]

#cursor.execute("""INSERT INTO next VALUES (?, ?, ?, ?, ?)""", info)

#cursor.execute("""DELETE FROM next WHERE location='BBB'""")

#info = cursor.execute("""SELECT * FROM next""")
#data = info.fetchall()
#print(data)

db.commit()