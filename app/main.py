
from fastapi import FastAPI
from sqlalchemy import log
from blog import  models
from blog.database import  engine
from blog.routers import blog, user, login


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(login.router)
app.include_router(blog.router)
app.include_router(user.router)

