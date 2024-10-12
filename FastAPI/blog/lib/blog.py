from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from .. import models, schemas  # pylint: disable=relative-beyond-top-level
from ..hashing import Hash


hash_util = Hash()


def get_blog(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create_blog(db: Session, blog: schemas.Blog, current_user: schemas.User):
    new_blog = models.Blog(title=blog.title, body=blog.body, creator_id=current_user.name)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete_blog(db: Session, _id: int):
    blog = db.query(models.Blog).filter(models.Blog._id == _id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with _id {_id} not found"
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def update_blog(db: Session, _id: int, blog: schemas.Blog):
    blog_to_update = db.query(models.Blog).filter(models.Blog._id == _id)
    if not blog_to_update.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with _id {_id} not found"
        )
    blog_to_update.update(dict(blog))
    db.commit()
    return Response(status_code=status.HTTP_202_ACCEPTED)


def get_blog_by__id(db: Session, _id: int):
    blog = db.query(models.Blog).filter(models.Blog._id == _id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with _id {_id} not found"
        )
    return blog
