import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
UPDATE servicos
SET foto = 'brasileiro.jpg'
WHERE nome = 'Volume Brasileiro'
""")

conn.commit()
conn.close()

print("Foto atualizada!")