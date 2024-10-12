from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, models
from sqlalchemy.orm import Session
from ..database import get_db
from ..hashing import Hash
from ..lib import user
router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.get("/{id}", response_model=schemas.User)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user_by_id(db, id)

@router.post("/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(db, request)