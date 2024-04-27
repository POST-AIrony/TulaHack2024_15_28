from pydantic import BaseModel


class SignUpRequest(BaseModel):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str


class SignInRequest(BaseModel):
    email: str
    password: str


class CreateChatRequest(BaseModel):
    token: str
    title: str
    is_public: bool
    is_accepted: bool


class NewMessageRequest(BaseModel):
    token: str
    chat_id: int
    message: str


class EditMessageRequest(BaseModel):
    token: str
    chat_id: int
    message: str
    message_id: int


class GetMessageRequest(BaseModel):
    token: str
    chat_id: int