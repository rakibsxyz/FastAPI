from fastapi import APIRouter, status, Depends, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..hashing import Hash

def create(request, db: Session):
    newUser = models.User(name=request.name, email=request.email, password= Hash.bcrypt(request.password))
    # newUser = models.User(request)
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser


def show(id, db):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f"blog with id {id} not found"}

    return user



def showAll(db: Session):
    user = db.query(models.User).all()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f"blog with id {id} not found"}

    return user