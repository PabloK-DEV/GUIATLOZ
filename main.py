from fastapi import FastAPI, HTTPException
from typing import Union
import uvicorn
import requests

app = FastAPI()

# --- DEFINIÇÃO DA CLASSE (A estrutura do seu sistema) ---


# --- AS ROTAS (@app.get) --- '''

@app.get("/")
def home():
    return {"status": "aqui", "docs": "/docs"}

@app.get("/item/{name}")
def read_item(name: str):
    print('chegou aqui')
    try:
        data = requests.get(f'https://botw-compendium.herokuapp.com/api/v3/compendium/entry/{name}')
        return data.json()
    except Exception as e:
        print (str (e))
        raise HTTPException(status_code=404, detail=str(e))