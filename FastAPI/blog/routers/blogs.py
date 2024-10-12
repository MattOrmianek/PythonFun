from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, models
from sqlalchemy.orm import Session
from fastapi import Response
from ..database import get_db
from ..hashing import Hash
from ..lib import blog
from ..oauth2 import get_current_user
router = APIRouter(
    prefix="/blog",
    tags=["blogs"]
)

@router.post("/blog", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.create_blog(db, request)

@router.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    return blog.delete_blog(db, id)

@router.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update_blog(db, id, request)

@router.get("/blog")
def get_all_blogs(db: Session = Depends(get_db)):
    return blog.get_blog(db)

@router.get("/blog/{id}", response_model=schemas.Blog)
def get_blog(id: int, db: Session = Depends(get_db)):
    return blog.get_blog_by_id(db, id)


