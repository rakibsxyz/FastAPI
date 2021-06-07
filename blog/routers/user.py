from fastapi import APIRouter, status, Depends, HTTPException
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..repository import user

router = APIRouter(tags=["Users"])


get_db = database.get_db


@router.post('/user',status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser,  )
def createUser(request: schemas.User, db: Session = Depends(get_db)):
   return user.create(request, db)


@router.get('/user/{id}', response_model=schemas.ShowUser, status_code=status.HTTP_200_OK,  )
def showUser(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)

@router.get('/userall', response_model=List[schemas.ShowUser], status_code=status.HTTP_200_OK,  )
def showUser( db: Session = Depends(get_db)):
   return user.showAll(db)