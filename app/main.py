import requests
from fastapi import FastAPI, Depends
from .routers import category, root as root_router
from .dependencies import get_token_header
from .internal import admin
from app.routers import items, users
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(version="0.0.5")

origins = [
    "http://localhost",
    "http://localhost:*",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:5173",
    # "https://hyrule-wiki.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex="https://.*\\.vercel\\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(root_router.router)
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
