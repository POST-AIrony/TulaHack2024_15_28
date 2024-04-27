import asyncio

from tortoise import Model, Tortoise, fields


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100)
    password = fields.CharField(max_length=100)
    first_name = fields.CharField(max_length=100)
    last_name = fields.CharField(max_length=100)
    is_admin = fields.BooleanField(default=False)

    async def json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "first_name": self.last_name,
            "is_admin": self.is_admin,
        }


class Chat(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    conversation = fields.JSONField()
    user_id = fields.ForeignKeyField("models.User")
    is_public = fields.BooleanField(default=False)
    is_accepted = fields.BooleanField(default=False)


class PublicChat(Model):
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
