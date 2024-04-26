import asyncio

import jwt
from fastapi import FastAPI
from ml import ml_pass
from models.models import Chat, User
from schemas import CreateChatRequest, NewMessageRequest, SignInRequest, SignUpRequest
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


secret_key = "allelleo"

app = FastAPI(title="TulaHack", lifespan=lifespan)


@app.post("/sign-in")
async def sign_in(data: SignInRequest):

    try:
        user = await User.get(email=data.email)
    except:
        raise
    if not user.password == data.password:
        raise
    return {
        "token": jwt.encode(
            {"user_id": user.id},
            secret_key,
            algorithm="HS256",
            headers={"alg": "HS256", "typ": "JWT"},
        ).encode("utf-8")
    }


@app.post("/sign-up")
async def sign_up(data: SignUpRequest):
    if await User.exists(username=data.username):
        raise

    if await User.exists(email=data.email):
        raise

    user = User(
        username=data.username,
        email=data.email,
        password=data.password,
        first_name=data.first_name,
        last_name=data.last_name,
    )

    await user.save()

    return {"user_id": user.id}


@app.post("/protected")
async def protected(token: str):
    decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
    user_id = decoded_token.get("user_id")
    user = await User.get(id=user_id)
    return user


@app.post("/chat")
async def create_chat(data: CreateChatRequest):
    decoded_token = jwt.decode(data.token, secret_key, algorithms=["HS256"])
    user_id = decoded_token.get("user_id")
    user = await User.get(id=user_id)
    chat = Chat(
        title=data.title,
        conversation={},
        is_public=data.is_public,
        is_accepted=data.is_accepted,
        user_id=user,
    )

    await chat.save()

    chats = []
    for chat in await Chat.filter(user_id=user):
        messages = len(chat.conversation) // 2
        chats.append({"title": chat.title, "messages_count": messages})
    return chats


@app.get("/chats")
async def get_chats(token: str):
    decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
    user_id = decoded_token.get("user_id")
    user = await User.get(id=user_id)

    chats = []
    for chat in await Chat.filter(user_id=user):
        messages = len(chat.conversation) // 2
        chats.append({"title": chat.title, "messages_count": messages})
    return chats


@app.post("/chat/message")
async def new_message(data: NewMessageRequest):
    decoded_token = jwt.decode(data.token, secret_key, algorithms=["HS256"])
    user_id = decoded_token.get("user_id")
    user = await User.get(id=user_id)

    chat = await Chat.get(id=data.chat_id)
    messages = chat.conversation
    messages.append({"role": "user", "message": data.message})

    #! TODO SEND MESSAGES TO ML
    messages, answer = ml_pass(messages)
    chat.messsages = messages
    await chat.save()
    return {"answer": answer}


import uvicorn

# if __name__ == "__main__":
#     uvicorn.run(app)
