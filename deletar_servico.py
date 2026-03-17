import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM servicos WHERE rowid = 56")
cursor.execute("DELETE FROM servicos WHERE rowid = 57")
cursor.execute("DELETE FROM servicos WHERE rowid = 58")

conn.commit()

print("3 serviços específicos deletados!")

conn.close()