import asyncio

from tortoise import Model, Tortoise, fields


class User(Model):
    """
    Модель пользователя.

    Attributes:
    - id (int): Идентификатор пользователя.
    - email (str): Электронная почта пользователя.
    - password (str): Пароль пользователя.
    - is_admin (bool): Флаг, указывающий является ли пользователь администратором.

    Methods:
    - async def json(self): Возвращает данные пользователя в формате JSON.
    """
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=100)
    password = fields.CharField(max_length=100)
    is_admin = fields.BooleanField(default=False)

    async def json(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_admin": self.is_admin,
        }


class Chat(Model):
    """
    Модель чата.

    Attributes:
    - id (int): Идентификатор чата.
    - title (str): Название чата.
    - conversation (list): Список сообщений в чате.
    - user_id (User): Идентификатор пользователя, создавшего чат.
    - is_public (bool): Флаг, указывающий является ли чат публичным.
    - is_accepted (bool): Флаг, указывающий принят ли чат.

    """
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    conversation = fields.JSONField()
    user_id = fields.ForeignKeyField("models.User")
    is_public = fields.BooleanField(default=False)
    is_accepted = fields.BooleanField(default=False)


class PublicChat(Model):
    """
    Модель публичного чата.

    Attributes:
    - id (int): Идентификатор публичного чата.
    - title (str): Название публичного чата.
    - conversation (list): Список сообщений в публичном чате.
    - user_id (User): Идентификатор пользователя, создавшего публичный чат.
    - is_accepted (bool): Флаг, указывающий принят ли публичный чат.

    Methods:
    - async def json(self): Возвращает данные публичного чата в формате JSON.
    """
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    conversation = fields.JSONField()
    user_id = fields.ForeignKeyField("models.User")
    is_accepted = fields.BooleanField(default=False)

    async def json(self):
        user = await self.user_id.get()
        return {
            "id": self.id,
            "title": self.title,
            "conversation": self.conversation,
            "user_id": await user.json(),
            "is_accepted": self.is_accepted,
        }


class Chat28(Model):
    """
    Модель чата 28.

    Attributes:
    - id (int): Идентификатор чата 28.
    - title (str): Название чата 28.
    - manager_conversation (list): Список сообщений в чате 28.
    - bot_answer (str): Ответ бота в чате 28.
    - user_id (User): Идентификатор пользователя, создавшего чат 28.

    Methods:
    - async def json(self): Возвращает данные чата 28 в формате JSON.
    """ 
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    manager_conversation = fields.JSONField()
    bot_answer = fields.TextField(nulll=True)
    user_id = fields.ForeignKeyField("models.User")

    async def json(self):
        user = await self.user_id.get()
        return {
            "id": self.id,
            "title": self.title,
            "manager_conversation": self.manager_conversation,
            "bot_answer": self.bot_answer,
            "user_id": await user.json(),
        }
