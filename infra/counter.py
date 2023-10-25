if __name__ == "__main__":
    app.run(host="0.0.0.0")
Si votre objectif est d'ouvrir le fichier HTML (`ShopifyShop.html`) à partir de votre script Python (`counter.py`), vous pouvez utiliser un module Python tel que `webbrowser` pour ouvrir le fichier HTML dans le navigateur par défaut de la machine où le script est exécuté. Voici comment vous pouvez le faire dans votre script Python :

```python
import webbrowser

# Spécifiez le chemin vers le fichier HTML
html_file = "ShopifyShop.html"

# Utilisez la fonction open de webbrowser pour ouvrir le fichier HTML
webbrowser.open(html_file)
```
