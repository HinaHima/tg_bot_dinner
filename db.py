#importing the database
import sqlite3

db = sqlite3.connect("next.db")
cursor = db.cursor()