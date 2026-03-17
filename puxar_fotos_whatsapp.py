from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import os

# link do catálogo
url = "https://wa.me/c/5519971577772"  # coloque seu número

# criar pasta
os.makedirs("fotos_catalogo", exist_ok=True)

# iniciar navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

print("Abrindo catálogo...")

driver.get(url)

# esperar carregar
time.sleep(10)

# pegar imagens
imgs = driver.find_elements(By.TAG_NAME, "img")

print("Imagens encontradas:", len(imgs))

contador = 0

for img in imgs:

    src = img.get_attribute("src")

    if src and "https" in src:

        try:
            r = requests.get(src)

            with open(f"fotos_catalogo/foto_{contador}.jpg", "wb") as f:
                f.write(r.content)

            print("baixado:", contador)

            contador += 1

        except:
            pass

print("Download finalizado")

time.sleep(5)

driver.quit()