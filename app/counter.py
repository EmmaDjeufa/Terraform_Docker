from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# Obtenez le répertoire actuel où se trouve le fichier counter.py
current_directory = os.path.dirname(os.path.realpath(__file__))

# Construisez le chemin complet du fichier HTML
#html_file_path = os.path.join(current_directory, "ShopifyShop.html")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("ShopifyShop.html", "r") as html_file:
        return html_file.read()

