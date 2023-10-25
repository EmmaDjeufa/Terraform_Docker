from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    try:
        with open("app/ShopifyShop.html", "r") as html_file:
            return html_file.read()
    except FileNotFoundError:
        # Afficher un message d'erreur si le fichier n'existe pas
        return "Fichier HTML introuvable", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
