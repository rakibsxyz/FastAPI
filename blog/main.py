from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from . import schemas, models
from . database import SessionLocal, engine
app = FastAPI()

models.Base.metadata.create_all(engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post('/blog')
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    newBlog = models.Blog(title=request.title, body=request.body)
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog)
    return newBlog
    
    
    # return { 'title': request.title, 'body': request.body}