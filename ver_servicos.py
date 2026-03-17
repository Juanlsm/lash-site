import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM servicos")

servicos = cursor.fetchall()

for s in servicos:
    print(s)

conn.close()