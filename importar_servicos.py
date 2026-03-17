import requests
import json
import sqlite3

url = "https://www.salonsoftware.com.br/api/agendamentoonline/get_inicial/luuadesignerr_"

headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(url, headers=headers)

dados = json.loads(res.text.encode().decode("utf-8-sig"))

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

print("Campos encontrados na API:")

for chave in dados:
    print(chave)

servicos = dados.get("servicos") or dados.get("services") or []

for s in servicos:

    nome = s.get("nome") or s.get("name")
    preco = s.get("preco") or s.get("price")

    cursor.execute("""
    INSERT INTO servicos (nome, preco)
    VALUES (?, ?)
    """, (nome, preco))

    print(f"Importado: {nome} - R$ {preco}")

conn.commit()
conn.close()

print("Importação finalizada")