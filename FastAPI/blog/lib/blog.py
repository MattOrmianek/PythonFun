from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status, Response
def get_blog(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create_blog(db: Session, blog: schemas.Blog):
    new_blog = models.Blog(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete_blog(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def update_blog(db: Session, id: int, blog: schemas.Blog):
    blog_to_update = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog_to_update.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog_to_update.update(dict(blog))
    db.commit()
    return Response(status_code=status.HTTP_202_ACCEPTED)

def get_blog_by_id(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    return blog