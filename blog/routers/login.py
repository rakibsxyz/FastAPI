from fastapi.exceptions import HTTPException
from blog.database import get_db
from fastapi.param_functions import Depends
from blog import models, schemas
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..hashing import Hash




router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login")
def login(request:schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials")
    
    if not Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid password")
    
    return user
