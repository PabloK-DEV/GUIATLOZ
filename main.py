from fastapi import FastAPI, HTTPException
from typing import Union
# Importe aqui as outras dependências que seu código usa (api, types, exceptions, etc)

app = FastAPI()

# --- DEFINIÇÃO DA CLASSE (A estrutura do seu sistema) ---
class Compendium:
    def __init__(self, base_url: str = "https://botw-compendium.herokuapp.com/api/v2"):
        self.base_url = base_url
        # Nota: Você precisará garantir que a classe 'api' e 'exceptions' estejam acessíveis aqui

    def get_entry(self, entry: str) -> dict:
        # Sua lógica de requisição aqui
        # Exemplo simplificado:
        import requests
        res = requests.get(f"{self.base_url}/entry/{entry}")
        return res.json()

    def get_category(self, category: str) -> dict:
        if category not in ["creatures", "equipment", "materials", "monsters", "treasure"]:
            raise ValueError("Categoria inválida")
        import requests
        res = requests.get(f"{self.base_url}/category/{category}")
        return res.json()

# --- INSTÂNCIA DO SISTEMA ---
botw = Compendium()

# --- AS ROTAS (@app.get) ---

@app.get("/")
def home():
    return {"status": "API do Zelda Online", "docs": "/docs"}

@app.get("/item/{name}")
def read_item(name: str):
    try:
        data = botw.get_entry(name)
        return data
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/categoria/{cat}")
def read_category(cat: str):
    try:
        return botw.get_category(cat)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))