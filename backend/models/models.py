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


class Conversation(Model):
    id = fields.IntField(pk=True)
    conversation = fields.JSONField()
    user_id = fields.ForeignKeyField("models.User")
    is_public = fields.BooleanField(default=True)
    is_accepted = fields.BooleanField(default=True)
    parent_conversation = fields.IntField()
