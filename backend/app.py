import asyncio

import jwt
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from ml import ml_pass
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
        conversation=[],
        is_public=data.is_public,
        is_accepted=data.is_accepted,
        user_id=user,
    )

    await chat.save()

    chats = []
    for chat in await Chat.filter(user_id=user):
        messages = len(chat.conversation) // 2
        chats.append(
            {"chat_id": chat.id, "title": chat.title, "messages_count": messages}
        )
    return chats


@app.get("/chats")
async def get_chats(token: str):
    decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
    user_id = decoded_token.get("user_id")
    user = await User.get(id=user_id)

    chats = []
    for chat in await Chat.filter(user_id=user):
        messages = len(chat.conversation) // 2
        chats.append(
            {"chat_id": chat.id, "title": chat.title, "messages_count": messages}
        )
    return chats


@app.post("/chat/message")
async def new_message(data: NewMessageRequest):
    decoded_token = jwt.decode(data.token, secret_key, algorithms=["HS256"])
    user_id = decoded_token.get("user_id")
    user = await User.get(id=user_id)

    chat = await Chat.get(id=data.chat_id)
    messages = chat.conversation
    messages_count = get_count_of_user_messages(messages)

    messages.append(
        {"role": "user", "message": data.message, "msg_id": messages_count + 1}
    )

    #! TODO SEND MESSAGES TO ML
    messages, answer = ml_pass(messages)
    chat.messsages = messages
    await chat.save()
    return {"answer": answer}


@app.post("/chat/message/edit")
async def edit_message(data: EditMessageRequest):
    decoded_token = jwt.decode(data.token, secret_key, algorithms=["HS256"])
    user_id = decoded_token.get("user_id")
    user = await User.get(id=user_id)

    chat = await Chat.get(id=data.chat_id)
    messages = chat.conversation
    new_messages = []
    for message in messages:
        print(message)
        if message["role"] == "user":
            if message["msg_id"] == data.message_id:
                new_messages.append(
                    {"role": "user", "message": data.message, "msg_id": data.message_id}
                )
                break
            else:
                new_messages.append(message)
        else:
            new_messages.append(message)

    messages, answer = ml_pass(new_messages)
    chat.conversation = new_messages
    print(new_messages)
    await chat.save()
    chat = await Chat.get(id=data.chat_id)
    return {"answer": answer, "messages": chat.conversation}


@app.get("/chat/message")
async def get_message(token: str, chat_id: int):
    decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
    user_id = decoded_token.get("user_id")
    user = await User.get(id=user_id)

    chat = await Chat.get(id=chat_id)
    messages = chat.conversation

    return {"messages": messages}


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
