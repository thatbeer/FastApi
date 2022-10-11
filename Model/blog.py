from lib2to3.pytree import Base
from pydantic import BaseModel
from typing import List , Dict, Optional ,Set 



class Image(BaseModel):
    url: str
    alias : str

class BlogModel(BaseModel):
    title: str
    content: str
    published : bool | None
    nb_comments: int
    tags : List[str] = []
    metadata : Dict[str,str] = {'key1':'val1'}
    image: Image | None = None 