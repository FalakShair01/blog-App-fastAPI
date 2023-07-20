from typing import List
from pydantic import BaseModel


class User(BaseModel):
    name : str
    email : str
    password: str



class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config():
        orm_mode = True


class showBlog(Blog):
    class Config():
        orm_mode = True


class showUser(BaseModel):
    name: str
    email : str
    blogs : List[Blog] = []
    class Config():
        orm_mode = True


class showBlog(BaseModel):
    title: str
    body: str
    creator: showUser
    class Config():
        orm_mode = True


class Login(BaseModel):
    email: str
    password: str



#JWT Models
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None

