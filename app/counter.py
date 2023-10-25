#!/usr/bin/env python
from flask import Flask, send_file
import os
import redis

app = Flask(__name__)

# Vous pouvez spécifier le nom du service Docker FastAPI dans votre fichier docker-compose.yml.
# Par exemple, si votre service FastAPI est nommé "app" :
fastapi_service_name = "app"

# Utilisez le nom du service FastAPI dans l'URL pour accéder à l'API FastAPI depuis le conteneur Flask.
fastapi_url = f"http://{fastapi_service_name}:5000"

@app.route("/")
def index():
    # Définir le chemin du fichier HTML
    html_file = "ShopifyShop.html"

    # Vérifier si le fichier existe
    if os.path.exists(html_file):
        # Utiliser Flask pour renvoyer le fichier HTML
        return send_file(html_file)
    else:
        # Afficher un message d'erreur si le fichier n'existe pas
        return "Fichier HTML introuvable", 404

if __name__ == "__main__":
    # Exécutez Flask avec le port 80, car Flask fonctionnera dans un conteneur séparé.
    app.run(host="0.0.0.0")
