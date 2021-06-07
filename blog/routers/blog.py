from fastapi import APIRouter, status, Depends, HTTPException
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from .. repository import blog



router = APIRouter(
    prefix="/blog",
    tags=["blogs"]
    )


get_db = database.get_db

@router.get('/',status_code=status.HTTP_200_OK, response_model= List[schemas.ShowBlog] )
def showAllBlog(db: Session = Depends(database.get_db)):
    return blog.showAll(db)  


@router.post('/',status_code=status.HTTP_201_CREATED,  )
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request,db)
    

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED )
def updateBlog(id, request : schemas.Blog, db : Session = Depends(get_db)):
   return blog.update(id, request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model= schemas.ShowBlog )
def getSpecificBlog(id, db: Session = Depends(get_db)):
    return blog.show(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT )
def deleteBlog(id, db : Session = Depends(get_db)):
    return blog.delete(id, db)
   