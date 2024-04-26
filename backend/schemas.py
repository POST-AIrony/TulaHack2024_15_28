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
