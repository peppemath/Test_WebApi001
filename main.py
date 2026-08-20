from fastapi import FastAPI

app = FastAPI(title="Test Web API")

@app.get("/")
def home():
    return {"message": "Ciao, l'API funziona"}


@app.get("/saluta/{nome}")
def saluta(nome: str):
    return {"saluto": f"Ciao, {nome}"}

@app.get("/stato")
def stato():
    return {"ok": True}

