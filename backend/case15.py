import jwt
from constant import secret_key
from fastapi import APIRouter, HTTPException
from just_model import model
from ml import interact_history
from models.models import Chat, PublicChat, User
from schemas import (
    ChatCreate,
    CreateChatRequest,
    EditMessageRequest,
    NewMessageRequest,
    PublicChatCreate,
    SignInRequest,
    SignUpRequest,
)


def get_count_of_user_messages(messages):
    """
    Получает количество сообщений от пользователя в списке сообщений.

    Parameters:
    - messages (list): Список сообщений.

    Returns:
    - int: Количество сообщений от пользователя.
    """
    count = 0
    for msg in messages:
        if msg["role"] == "user":
            count += 1
    return count


case15 = APIRouter(prefix="/case15")


@case15.post("/sign-in")
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


@case15.post("/sign-up")
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


@case15.post("/protected")
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


@case15.post("/chat")
async def create_chat(data: CreateChatRequest):
    """
    Создает новый чат.

    Parameters:
    - data (CreateChatRequest): Объект, содержащий данные для создания чата.

    Returns:
    - list: Список чатов пользователя в формате JSON.

    Raises:
    - HTTPException: Ошибка HTTP с кодом статуса 404, если чаты пользователя не найдены.
    """
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


@case15.get("/chats")
async def get_chats(token: str):
    """
    Получает список чатов пользователя.

    Parameters:
    - token (str): JWT-токен для аутентификации пользователя.

    Returns:
    - list: Список чатов пользователя в формате JSON.

    Raises:
    - HTTPException: Ошибка HTTP с кодом статуса 404, если чаты пользователя не найдены.
    """
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


@case15.post("/chat/message")
async def new_message(data: NewMessageRequest):
    """
    Добавляет новое сообщение в чат и возвращает ответ от бота.

    Parameters:
    - data (NewMessageRequest): Объект, содержащий данные о новом сообщении в чате.

    Returns:
    - dict: Словарь с ответом от бота.

    Raises:
    - HTTPException: Ошибка HTTP с кодом статуса 404, если чат не найден.
    """
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
    answer = interact_history(model, messages)  # "test"
    chat.conversation.append({"role": "bot", "message": answer})
    await chat.save()
    return {"answer": answer}


@case15.post("/chat/message/edit")
async def edit_message(data: EditMessageRequest):
    """
    Редактирует сообщение в чате и возвращает ответ от бота.

    Parameters:
    - data (EditMessageRequest): Объект, содержащий данные для редактирования сообщения в чате.

    Returns:
    - dict: Словарь с ответом от бота и обновленными сообщениями чата.

    Raises:
    - HTTPException: Ошибка HTTP с кодом статуса 404, если чат не найден.
    """
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

    answer = interact_history(model, new_messages)
    new_messages.append({"role": "bot", "message": answer})
    chat.conversation = new_messages
    print(new_messages)
    await chat.save()
    chat = await Chat.get(id=data.chat_id)
    return {"answer": answer, "messages": chat.conversation}


@case15.get("/chat/message")
async def get_message(token: str, chat_id: int):
    """
    Получает сообщения чата по его идентификатору.

    Parameters:
    - token (str): JWT-токен для аутентификации пользователя.
    - chat_id (int): Идентификатор чата.

    Returns:
    - dict: Словарь с сообщениями чата.

    Raises:
    - HTTPException: Ошибка HTTP с кодом статуса 404, если чат не найден.
    """
    decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
    user_id = decoded_token.get("user_id")
    user = await User.get(id=user_id)

    chat = await Chat.get(id=chat_id)
    messages = chat.conversation

    return {"messages": messages}


@case15.post("/chat/toPublic")
async def send_chat_to_public(data: PublicChatCreate):
    """
    Переводит чат в публичный чат.

    Parameters:
    - data (PublicChatCreate): Объект, содержащий данные для перевода чата в публичный.

    Returns:
    - dict: Словарь с информацией о статусе операции.

    Raises:
    - HTTPException: Ошибка HTTP с кодом статуса 404, если чат не найден.
    """
    decoded_token = jwt.decode(data.token, secret_key, algorithms=["HS256"])
    user_id = decoded_token.get("user_id")
    user = await User.get(id=user_id)

    chat = await Chat.get(id=data.chat_id)
    public_chat = PublicChat(
        title=chat.title, conversation=chat.conversation, user_id=user
    )
    await public_chat.save()

    return {"status": "ok"}


@case15.get("/chat/public/moderation")
async def send_chat_to_public(token: str, public_id: int):
    """
    Модерирует публичный чат, подтверждая его публикацию.

    Parameters:
    - token (str): JWT-токен для аутентификации пользователя.
    - public_id (int): Идентификатор публичного чата.

    Returns:
    - dict: Словарь с информацией о статусе операции.

    Raises:
    - HTTPException: Ошибка HTTP с кодом статуса 401, если пользователь не является администратором.
    - HTTPException: Ошибка HTTP с кодом статуса 404, если публичный чат не найден.
    """
    decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
    user_id = decoded_token.get("user_id")
    user = await User.get(id=user_id)

    if not user.is_admin:
        raise HTTPException(status_code=401, detail="not admin")

    public_chat = await PublicChat.get(id=public_id)
    public_chat.is_accepted = True
    await public_chat.save()
    return {"status": "ok"}


@case15.get("/chat/public/moderation/all")
async def send_chat_to_public(token: str):
    """
    Получает список всех публичных чатов для модерации.

    Parameters:
    - token (str): JWT-токен для аутентификации пользователя.

    Returns:
    - list: Список публичных чатов в формате JSON.

    Raises:
    - HTTPException: Ошибка HTTP с кодом статуса 401, если пользователь не является администратором.
    """
    decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
    user_id = decoded_token.get("user_id")
    user = await User.get(id=user_id)

    if not user.is_admin:
        raise HTTPException(status_code=401, detail="not admin")
    data = []
    public_chat = await PublicChat.all()
    for chat in public_chat:
        data.append(await chat.json())
    return data


@case15.get("/chat/public")
async def get_publics(start: int, stop: int):
    """
    Получает список публичных чатов в указанном диапазоне идентификаторов.

    Parameters:
    - start (int): Начальный идентификатор чата.
    - stop (int): Конечный идентификатор чата.

    Returns:
    - list: Список публичных чатов в указанном диапазоне идентификаторов.

    Raises:
    - HTTPException: Ошибка HTTP с кодом статуса 404, если чаты не найдены.
    """
    chats = await PublicChat.filter(is_accepted=True)
    data = []
    for chat in chats:
        if chat.id in range(start, stop):
            data.append(await chat.json())
    return data


@case15.post("/chat/copy")
async def copy_chat(data: ChatCreate):
    """
    Копирует публичный чат для конкретного пользователя.

    Parameters:
    - data (ChatCreate): Объект, содержащий данные для копирования чата.

    Returns:
    - dict: Словарь с информацией о статусе операции.

    Raises:
    - HTTPException: Ошибка HTTP с кодом статуса 404, если публичный чат не найден.
    """
    decoded_token = jwt.decode(data.token, secret_key, algorithms=["HS256"])
    user_id = decoded_token.get("user_id")
    user = await User.get(id=user_id)

    public = await PublicChat.get(id=data.public_chat_id)
    user_chat = Chat(
        title=public.title,
        conversation=public.conversation,
        user_id=user,
    )

    await user_chat.save()

    return {"status": "ok"}
