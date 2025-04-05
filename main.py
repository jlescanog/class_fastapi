from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4 as uuid
from typing import Optional, Text


app = FastAPI()

posts = []

# Clase para Post Model
class Post(BaseModel):
    id: str
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False

# Clase para actualizar Post Model
class PostUpdate(BaseModel):
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()


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

# Endpotin para eleminar un post por su ID
@app.delete('/posts/delete/{post_id}')
def delete_post(post_id:str):
    for index, post in enumerate(posts):
        if post['id'] == post_id:
            posts.pop(index)
            return {'message':'Post eliminado satisfactoriamente'}
    raise HTTPException(status_code=404, detail='Post no encontrado')

# Endpoint para actualizar un post
@app.put('/posts/update/{post_id}')
def update_post(post_id:str, updatedPost:PostUpdate):
    for post in posts:
        if post['id'] == post_id:
            post.update(updatedPost.dict())
            return {'message':'Post actualizado correctamente'}
    raise HTTPException(status_code=404, detail='Post no encontrado')