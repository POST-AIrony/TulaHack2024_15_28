import asyncio

import jwt
from fastapi import FastAPI
from tortoise import Model, Tortoise, fields

from .schemas import SignInRequest, SignUpRequest


async def init():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",  # Подставьте путь к файлу SQLite
        modules={
            "models": ["models.models"]
        },  # Подставьте имя модуля, где определены ваши модели
    )
    await Tortoise.generate_schemas()


async def lifespan(app: FastAPI):
    await init()
    yield


app = FastAPI(title="TulaHack", lifespan=lifespan)


@app.post("/sign-in")
async def sign_in(data: SignInRequest):
    pass


@app.post("/sign-up")
async def sign_up(data: SignUpRequest):
    pass


import uvicorn

if __name__ == "__main__":
    uvicorn.run(app)
