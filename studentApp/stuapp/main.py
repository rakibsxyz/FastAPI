
from fastapi import FastAPI, Depends
from sqlalchemy import schema
from sqlalchemy.sql.functions import count, mode
import models, schemas
from database import engine, get_db
from sqlalchemy.orm import Session

import json

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.post('/student',tags=["Student"])
def createStu(request: schemas.ShowStudent, db: Session= Depends(get_db)):
    newStu = models.Student(stuId= request.stuId, name=request.name)
    db.add(newStu)
    db.commit()
    db.refresh(newStu)
    return newStu

@app.get('/student', tags=["Student"])
def getAllStudent(db: Session= Depends(get_db)):
    students = db.query(models.Student).all()
    return students


@app.put('/student/{id}', tags=["Student"])
def updateStudent(request:schemas.ShowStudent, id:int, db: Session= Depends(get_db)):
    db.query(models.Student).filter(models.Student.stuId== id).update({'name': request.name})
    db.commit()
    return "done updating"

@app.delete('/student/{id}', tags=["Student"])
def deleteStudent(id, db: Session= Depends(get_db)):
    db.query(models.Student).filter(models.Student.stuId==id).delete(synchronize_session=False)
    db.commit()
    return "done deleting"


# activity

@app.post('/activity',tags=["Activity"])
def createActivity(request: schemas.Activity, db: Session= Depends(get_db)):
    newActivity = models.Activity(activity= request.activity, cost= request.cost)
    db.add(newActivity)
    db.commit()
    db.refresh(newActivity)
    return newActivity


@app.get('/activity', tags=["Activity"])
def getAllActivity(db: Session= Depends(get_db)):
    activity = db.query(models.Activity).all()
    return activity


@app.put('/activity/{name}', tags=["Activity"])
def updateActivity(request:schemas.Activity, name:str, db: Session= Depends(get_db)):
    db.query(models.Activity).filter(models.Activity.activity== name).update({'activity': request.activity, 'cost': request.cost})
    db.commit()
    return "done updating"

@app.delete('/activity/{name}', tags=["Activity"])
def deleteActivity(name, db: Session= Depends(get_db)):
    db.query(models.Activity).filter(models.Activity.activity==name).delete(synchronize_session=False)
    db.commit()
    return "done deleting"


# Participants
@app.post('/participant',tags=["Participant"])
def createParticipants(request: schemas.Participant, db: Session= Depends(get_db)):
    newParticipant = models.Participant(pid= request.pid, stuId= request.stuId, activity= request.activity)
    db.add(newParticipant)
    db.commit()
    db.refresh(newParticipant)
    return newParticipant


@app.get('/participant', tags=["Participant"])
def getAllParticipant(db: Session= Depends(get_db)):
    participant = db.query(models.Participant).all()
    return participant


@app.put('/participant/{id}', tags=["Participant"])
def updateParticipant(request:schemas.Participant, id:int, db: Session= Depends(get_db)):
    participant = db.query(models.Participant).filter(models.Participant.pid== id).update({'pid': request.pid,'stuId': request.stuId, 'activity': request.activity})
    if not participant:
        return "painai"
    db.commit()
    return "done updating"

@app.delete('/participant/{id}', tags=["Participant"])
def deleteParticipant(id, db: Session= Depends(get_db)):
    db.query(models.Participant).filter(models.Participant.pid==id).delete(synchronize_session=False)
    db.commit()
    return "done deleting"



# find those students who are taking X activity

@app.get('/students/{activity}',tags=["Mixed"])
def findStudentsWithActivity(activity: str, db: Session= Depends(get_db)):
    filteredActivity = db.query(models.Participant).filter(models.Participant.activity==activity).all()
    ids = []
    for act in filteredActivity:
        ids.append(act.stuId)

    students = db.query(models.Student).all()
    
    result =[]
    for stu in students:
        if stu.stuId in ids:
           result.append(stu.name)


    if not result:
        return "Students didnt participate in this activity"

    return result

# find activity count 
@app.get('/activity/count',tags=["Mixed"])
def findActivityCount(db: Session= Depends(get_db)):

    filteredActivity = db.query(models.Participant).all()
    
    filteredActivityList =[]
    for act in filteredActivity:
        filteredActivityList.append(act.activity)

    uniqActivity = set(filteredActivityList)
    
    activityList = []
    for x in uniqActivity:
        activityList.append(x)
    countList =[]
    for i in range (len(uniqActivity)):
        countList.append(filteredActivityList.count(activityList[i]))

    result = json.dumps([{'Activity':activity, 'Count':count} for  activity,count  in zip(activityList, countList)] )
    
    # jsonized = map(lambda item: {'Activity':item[0], 'Count':item[1]}, zip(activityList, countList))
    jsonList =[]
    # for i in range(0,len(countList)):
    #     jsonList.append({"country" : activityList[i], "wins" : countList[i]})


    # jsonized = json.dumps(jsonList, indent = 1)
    return result



# Find those users whose tatal fee >15 taka

