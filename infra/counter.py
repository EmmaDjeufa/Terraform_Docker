import os
import webbrowser

# Obtenez le chemin absolu du répertoire actuel (où se trouve counter.py)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Spécifiez le nom du fichier HTML et le chemin relatif vers le dossier "app"
html_file = os.path.join(current_directory, "app", "ShopifyShop.html")

# Utilisez la fonction open de webbrowser pour ouvrir le fichier HTML
webbrowser.open(html_file)
