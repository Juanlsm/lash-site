import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

print("\nSERVIÇOS CADASTRADOS:\n")

cursor.execute("SELECT * FROM servicos")

for linha in cursor.fetchall():
    print(linha)

conn.close()