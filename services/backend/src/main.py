from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from src.database.register import register_tortoise  # NEW
from src.database.config import TORTOISE_ORM         # NEW

# enable schemas to read relationship between models
Tortoise.init_models(["src.database.models"], "models")  # NEW

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://192.168.0.106:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# NEW
register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)


@app.get("/")
def home():
    return "Gokul Deepak!"