from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4 as uuid
from typing import Optional, Text


app = FastAPI()

posts = []

# Post Model
class Post(BaseModel):
    id: str
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False

@app.get("/")
def read_root():
    return {"Hello": "Bienvenido a mi API"}

@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts/create')
def create_post(post:Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return {'message': 'Post creado satisfactoriamente'}