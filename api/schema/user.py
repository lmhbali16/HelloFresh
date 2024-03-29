from typing import List
from pydantic import BaseModel
from pydantic.networks import EmailStr


class UserBase(BaseModel):
    name: str
    password: str
    email: EmailStr
    plans: List = []

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
