from fastapi import APIRouter

case28 = APIRouter()

import jwt
from constant import MODEL_PATH
from fastapi import APIRouter, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from llama_cpp import Llama
from ml import interact_manager
from models.models import Chat, Chat28, PublicChat, User
from schemas import CreateChat28, SignInRequest, SignUpRequest

secret_key = "allelleo"

model = Llama(
    model_path=MODEL_PATH,
    n_gpu_layers=-1,
    n_batch=512,
    n_ctx=4096,
    n_parts=1,
)


def text2json(dialog_str):
    """
    Функция для преобразования диалога клиент-сотрудник в формат JSON.

    Аргументы:
    dialog_str (str): Строка с диалогом клиент-сотрудник.

    Возвращает:
    str: Строка в формате JSON, представляющая диалог.
    """
    dialog_list = dialog_str.split("\n")
    dialog = []
    for line in dialog_list:
        speaker, message = line.split(": ")
        dialog.append((speaker.strip(), message.strip()))

    manager_conversation = []
    for speaker, message in dialog:
        manager_conversation.append({"speaker": speaker, "message": message})

    return manager_conversation


@case28.post("/sign-in")
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


@case28.post("/sign-up")
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


@case28.post("/protected")
async def protected(token: str):
    decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
    user_id = decoded_token.get("user_id")
    user = await User.get(id=user_id)
    return user


@case28.post("/chat")
async def create_chat(data: CreateChat28):
    decoded_token = jwt.decode(data.token, secret_key, algorithms=["HS256"])
    user_id = decoded_token.get("user_id")
    user = await User.get(id=user_id)
    json_conversation = text2json(data.dialog)
    answer = interact_manager(model)
    chat = Chat28(
        title=data.title,
        manager_conversation=json_conversation,
        user_id=user,
        bot_answer=answer,
    )
    await chat.save()

    data = {}

    data["manager_conversation"] = json_conversation
    data["answer"] = answer

    return data


@case28.get("/chat")
async def get_chats(token: str):
    decoded_token = jwt.decode(data.token, secret_key, algorithms=["HS256"])
    user_id = decoded_token.get("user_id")
    user = await User.get(id=user_id)

    chats = await Chat28.filter(user_id=user)
    data = []

    for chat in chats:
        data.append(await chat.json())

    return data


@case28.get("/chat/messages")
async def chat_messages(token: str, chat_id: int):
    decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
    user_id = decoded_token.get("user_id")
    user = await User.get(id=user_id)

    chat = await Chat28.get(id=chat_id)
    return await chat.json()
