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

#info = ["12.12.12", "BBB", "25 свободных", "3.500", "Секрет"]

#admin = ["Boris", 523492225]

#cursor.execute("DROP TABLE users")

#cursor.execute("""INSERT INTO admin VALUES (?, ?)""", admin)

#cursor.execute("""DELETE FROM next WHERE location='BBB'""")

cursor.execute("""SELECT * FROM next""")
data = cursor.fetchall()
print(data)

db.commit()