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
    """
    Выполняет аутентификацию пользователя.

    Parameters:
    - data (SignInRequest): Объект, содержащий данные для аутентификации.
    
    Returns:
    - dict: Словарь с JWT-токеном, содержащим идентификатор пользователя.

    Raises:
    - HTTPException: Ошибка HTTP с кодом статуса 404, если пользователь не найден.
    - HTTPException: Ошибка HTTP с кодом статуса 401, если указан неверный пароль.
    """
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
    """
    Регистрирует нового пользователя.

    Parameters:
    - data (SignUpRequest): Объект, содержащий данные для регистрации нового пользователя.

    Returns:
    - dict: Словарь с идентификатором созданного пользователя.

    Raises:
    - HTTPException: Ошибка HTTP с кодом статуса 409, если указанный email уже занят.
    """
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
    """
    Получает информацию о пользователе по JWT-токену.

    Parameters:
    - token (str): JWT-токен для аутентификации пользователя.

    Returns:
    - User: Объект пользователя.

    Raises:
    - HTTPException: Ошибка HTTP с кодом статуса 401, если токен недействителен.
    """
    decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
    user_id = decoded_token.get("user_id")
    user = await User.get(id=user_id)
    return user


@case28.post("/chat")
async def create_chat(data: CreateChat28):
    """
    Создает новый чат.

    Parameters:
    - data (CreateChat28): Объект, содержащий данные для создания чата.

    Returns:
    - dict: Словарь с информацией о созданном чате.

    Raises:
    - HTTPException: Ошибка HTTP с кодом статуса 400, если формат диалога неверный.
    """
    decoded_token = jwt.decode(data.token, secret_key, algorithms=["HS256"])
    user_id = decoded_token.get("user_id")
    user = await User.get(id=user_id)
    try:
        json_conversation = text2json(data.dialog)
    except:
        raise HTTPException(status_code=400, detail="wrong dialog")
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
    """
    Получает список чатов пользователя.

    Parameters:
    - token (str): JWT-токен для аутентификации пользователя.

    Returns:
    - list: Список чатов пользователя в формате JSON.

    Raises:
    - HTTPException: Ошибка HTTP с кодом статуса 404, если чаты не найдены.
    """
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
    """
    Получает сообщения чата по его идентификатору.

    Parameters:
    - token (str): JWT-токен для аутентификации пользователя.
    - chat_id (int): Идентификатор чата.

    Returns:
    - dict: Сообщения чата в формате JSON.

    Raises:
    - HTTPException: Ошибка HTTP с кодом статуса 404, если чат не найден.
    """
    decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
    user_id = decoded_token.get("user_id")
    user = await User.get(id=user_id)

    chat = await Chat28.get(id=chat_id)
    return await chat.json()
