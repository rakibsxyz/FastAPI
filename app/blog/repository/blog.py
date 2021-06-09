
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from .. import models

def show(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f"blog with id {id} not found"}

    return blog

def showAll(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request,db: Session):
    newBlog = models.Blog(title=request.title, body=request.body, userId = 1)
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog)
    return newBlog


def update(id, request, db: Session):
    db.query(models.Blog).filter(models.Blog.id == id).update({'title' : request.title})
    db.commit()
    return "done updating"


def delete(id, db : Session):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return "done"
