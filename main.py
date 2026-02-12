from fastapi import FastAPI, HTTPException
from typing import Union
import uvicorn
import requests

app = FastAPI()

# --- AS ROTAS (@app.get) --- 

@app.get("/")
def home():
    return {"tela principal": "aqui", "docs": "/docs"}

# --- ROTA PARA TODOS OS ITENS ---

# ---   ROTA PARA ITEM ---
@app.get("/entry/{name}")
def read_item(name: str):
    try:
        data = requests.get(f'https://botw-compendium.herokuapp.com/api/v3/compendium/entry/{name.lower()}')
        return data.json()
    except Exception as e:
        print (str ('e'))
        raise HTTPException(status_code=404, detail=str(e))

# --- ROTA PARA CATEGORIA ---
@app.get("/category/{category}")
def read_category(category: str):
    try:
        data = requests.get(f'https://botw-compendium.herokuapp.com/api/v3/compendium/category/{category.lower()}')
        return data.json()
    except Exception as e:
        print (str (e))
        raise HTTPException(status_code=404, detail=str(e))