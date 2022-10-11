
from re import S
from typing import List
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str
    
#article inside UserDisplay        
class Article(BaseModel):
    title: str
    content: str
    published: bool
    class Config():
        orm_mode = True
    
class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []
    class Config():
        orm_mode = True
## User inside Article display
class User(BaseModel):
    id: int
    username: str
    class Config():
        orm_mode = True
        
class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id : int
        
        
class ArticleDisplay(BaseModel):
    title: str 
    content: str
    published: bool
    user: User
    class Config():
        orm_mode = True
    