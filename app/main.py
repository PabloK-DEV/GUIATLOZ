from fastapi import FastAPI
import requests
from .routers import root, category

app = FastAPI()

app.include_router(root.router)
app.include_router(category.router)
