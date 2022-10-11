from fastapi import FastAPI 
from router import blog_post , blog_get , user , article
from db import models
from db.database import engine


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)

@app.get('/index') ## '/' > this is called path end point
def index():
    return {"hello" : "world"}

@app.post("/hello")
def post_index():
    return {"message":"HI MONDAy"}

models.Base.metadata.create_all(engine)
