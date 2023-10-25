#!/usr/bin/env python

from flask import Flask, send_file
import os
import redis

app = Flask(__name__)

redis_host = "redis"
redis_port = 6379

# Création d'une instance de connexion Redis
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=0)


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
    app.run(host="0.0.0.0" , port=5000)
