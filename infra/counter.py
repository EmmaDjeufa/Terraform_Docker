from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route("/")
def index():
    # Obtenez le chemin absolu du répertoire actuel
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Définir le nom du fichier HTML
    html_file = "ShopifyShop.html"

    # Combinez le chemin du répertoire actuel avec le nom du fichier
    html_path = os.path.join(current_directory, html_file)

    # Vérifiez si le fichier existe
    if os.path.exists(html_path):
        # Utilisez Flask pour renvoyer le fichier HTML
        return send_file(html_path)
    else:
        # Affichez un message d'erreur si le fichier n'existe pas
        return "Fichier HTML introuvable", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0")
