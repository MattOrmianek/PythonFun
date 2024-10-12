from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas
from ..database import get_db
from ..lib import user

router = APIRouter(prefix="/user", tags=["users"])


@router.get("/{_id}", response_model=schemas.User)
def get_user(_id: int, db: Session = Depends(get_db)):
    return user.get_user_by__id(db, _id)


@router.post("/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(db, request)
