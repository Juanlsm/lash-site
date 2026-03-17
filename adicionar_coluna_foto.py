import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
ALTER TABLE servicos
ADD COLUMN foto TEXT
""")

conn.commit()
conn.close()

print("Coluna foto criada!")