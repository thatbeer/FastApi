from xmlrpc.client import Boolean, ResponseError
from fastapi import FastAPI ,status , Response , APIRouter
from enum import Enum
from router import blog_post , blog_get
app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/index') ## '/' > this is called path end point
def index():
    return {"hello" : "world"}

@app.post("/hello")
def post_index():
    return {"message":"HI MONDAy"}
