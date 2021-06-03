from typing import List
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, responses, status, Response, HTTPException
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.functions import mode
from . import schemas, models
from . database import SessionLocal, engine
from . hashing import Hash
app = FastAPI()

models.Base.metadata.create_all(engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    newBlog = models.Blog(title=request.title, body=request.body)
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog)
    return newBlog
    
    
    # return { 'title': request.title, 'body': request.body}



@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def updateBlog(id, request : schemas.Blog, db : Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).update({'title' : request.title})
    db.commit()


    return "done updating"


@app.get('/blog',status_code=status.HTTP_200_OK, response_model= List[schemas.ShowBlog])
def showAllBlog(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs




@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model= schemas.ShowBlog)
def getSpecificBlog(id,response: Response,db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f"blog with id {id} not found"}

    return blog


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def deleteBlog(id, db : Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)

    db.commit()
    return "done"



# User
@app.post('/user',status_code=status.HTTP_201_CREATED)
def createUser(request: schemas.User, db: Session = Depends(get_db)):
    newUser = models.User(name=request.name, email=request.email, password= Hash.bcrypt(request.password))
    # newUser = models.User(request)
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser
