from fastapi import FastAPI
from . import models
from .database import engine, get_db
from . import schemas
from sqlalchemy.orm import Session
from fastapi import Depends

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post("/blog")
def create_blog(blog: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog")
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get("/blog/{id}")
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog