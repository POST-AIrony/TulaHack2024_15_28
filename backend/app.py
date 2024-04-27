import jwt
from case15 import case15
from case28 import case28
from constant import MODEL_PATH
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from llama_cpp import Llama
from models.models import Chat, User
from schemas import (
    CreateChatRequest,
    EditMessageRequest,
    GetMessageRequest,
    NewMessageRequest,
    SignInRequest,
    SignUpRequest,
)
from tortoise import Model, Tortoise, fields


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


def get_count_of_user_messages(messages):
    count = 0
    for msg in messages:
        if msg["role"] == "user":
            count += 1
    return count


secret_key = "allelleo"

app = FastAPI(title="TulaHack", lifespan=lifespan)

app.include_router(case15, tags=["case15"])
app.include_router(case28, tags=["case28"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# if __name__ == "__main__":
#     uvicorn.run(app)
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/html")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")
