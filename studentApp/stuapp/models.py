from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from database import Base


class Student(Base):
    __tablename__ = "students"
    stuId = Column(Integer,primary_key=True, index=True)
    name = Column(String)
    # body = Column(String)
    # userId = Column(Integer, ForeignKey('users.id'))

    # creator = relationship("User", back_populates="blogs")



class Activity(Base):
    __tablename__ = "activities"
    activity = Column(String,primary_key=True, index=True )
    cost = Column(Integer)


class Participant(Base):
    __tablename__ = "participants"
    pid = Column(Integer, primary_key=True,index=True)
    stuId = Column(Integer,ForeignKey('students.stuId'))
    activity = Column(String, ForeignKey('activities.activity'))

