from fastapi import APIRouter

case28 = APIRouter()

import jwt
from fastapi import APIRouter, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from models.models import Chat, Chat28, PublicChat, User
from schemas import CreateChat28, SignInRequest, SignUpRequest

secret_key = "allelleo"


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
    chat = Chat28(
        title=data.title,
        manager_conversation=data.dialog,
        user_id=user,
    )
    await chat.save()

    answer = "hello"  # TODO
    chat.bot_answer = answer
    await chat.save()

    return answer


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