from fastapi import FastAPI, Depends
import requests
from .routers import root, category
from .dependencies import get_query_token, get_token_header
from .internal import admin
from app.routers import items, users
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(version="0.0.3")

origins = [
    "http://localhost",
    "http://localhost:*",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:5173",
    "https://.*.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(root.router)
app.include_router(category.router)

app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
