from fastapi import FastAPI, HTTPException
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

# Endpoint para crear un nuevo post
@app.post('/posts/create')
def create_post(post:Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return {'message':'Post creado satisfactoriamente'}

# Endpoint para obtener un post por su ID
@app.get('/posts/{post_id}')
def get_post_by_id(post_id:str):
    for post in posts:
        if post['id'] == post_id:
            return post
    raise HTTPException(status_code=404, detail='Post no encontrado')

#