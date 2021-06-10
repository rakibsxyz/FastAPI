
from fastapi import FastAPI, Depends
from sqlalchemy import schema
import models, schemas
from database import engine, get_db
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.post('/')
def createStu(request: schemas.ShowStudent, db: Session= Depends(get_db)):
    newStu = models.Student(stuId= request.stuId, name=request.name)
    db.add(newStu)
    db.commit()
    db.refresh(newStu)
    return newStu

@app.post('/createAct')
def createActivity(request: schemas.Activity, db: Session= Depends(get_db)):
    newActivity = models.Activity(activity= request.activity, cost= request.cost)
    db.add(newActivity)
    db.commit()
    db.refresh(newActivity)
    return newActivity


@app.post('/createParticipants')
def createParticipants(request: schemas.Participant, db: Session= Depends(get_db)):
    newParticipant = models.Participant(pid= request.pid, stuId= request.stuId, activity= request.activity)
    db.add(newParticipant)
    db.commit()
    db.refresh(newParticipant)
    return newParticipant