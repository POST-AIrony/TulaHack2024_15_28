from fastapi import APIRouter

case28 = APIRouter()

import jwt
from constant import secret_key
from fastapi import APIRouter, HTTPException
from just_model import model
from ml import interact_manager
from models.models import Chat28, User
from schemas import CreateChat28, SignInRequest, SignUpRequest


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
        raise HTTPException(status_code=404, detail="user not found")
    if not user.password == data.password:
        raise HTTPException(status_code=401, detail="wrong password")
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
    if await User.exists(email=data.email):
        raise HTTPException(status_code=409, detail="email unique")

    user = User(
        email=data.email,
        password=data.password,
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
    answer = interact_manager(model, data.dialog)
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
    decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
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
