import os
import webbrowser

# Spécifier le chemin relatif pour accéder au fichier HTML
html_file = os.path.join('..', 'app', 'ShopifyShop.html')

# Utiliser la fonction open de webbrowser pour ouvrir le fichier HTML
webbrowser.open(html_file)
