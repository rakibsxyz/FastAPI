from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name':"Rakib"}}

@app.get('/about')
def about():
    return {'data': {'about page': "Nothing special man"}}

@app.get('/blogs')
def blogs(limit=10, published: bool= True, sort: Optional[str] = None ):
    if published:
        return {'blogs': {"id": "nai"}}
    else:
        return "not published"

@app.get('/blogs/unpublished')
def unpublished():
    return "unpublished"

@app.get('/blogs/{id}')
def blogId(id: int):
    return id

@app.get('/blogs/{id}/comments')
def blogComments(id):
    return 3


class Blog(BaseModel):
    title: str
    body: str
    published: Optional [bool]


@app.post('/createBlog')
def createBlog(request: Blog):
    return {'data': f"this is my blog title: {request.title}"}

