from fastapi import FastAPI
from . import models
from .database import engine
from .routers import users, blogs, auth

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(blogs.router)
app.include_router(auth.router)
