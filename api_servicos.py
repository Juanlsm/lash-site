import requests
import json

url = "https://www.salonsoftware.com.br/api/agendamentoonline/get_inicial/luuadesignerr_"

headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(url, headers=headers)

texto = res.text

dados = json.loads(texto.encode().decode("utf-8-sig"))

print(dados)