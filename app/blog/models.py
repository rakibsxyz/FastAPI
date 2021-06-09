
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from .database import Base


class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer,primary_key=True, index=True )
    title = Column(String)
    body = Column(String)
    userId = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blogs")



class User(Base): 
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("Blog", back_populates="creator")

