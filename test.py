#This file is used just to change the database
#importing the database
import sqlite3

#connecting to the db
db = sqlite3.connect("next.db")
#creating a cursor
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    tgID INTEGER NOT NULL
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS next(
    date TEXT NOT NULL,
    location TEXT NOT NULL,
    places TEXT NOT NULL,
    cost TEXT NOT NULL,
    film TEXT NOT NULL
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS admin(
    name TEXT NOT NULL,
    tgID INTEGER NOT NULL
)""")

#info = ["12.12.12", "BBB", "25 свободных", "3.500", "Секрет"]

#admin = ["Boris", 523492225]

#cursor.execute("DROP TABLE users")

#cursor.execute("""INSERT INTO admin VALUES (?, ?)""", admin)

#cursor.execute("""DELETE FROM next WHERE location='BBB'""")

cursor.execute("""SELECT name FROM admin WHERE tgID = 523492225""")
data = cursor.fetchall()

print(data)
db.commit()