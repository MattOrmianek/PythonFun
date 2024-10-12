from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas  # pylint: disable=relative-beyond-top-level
from ..hashing import Hash  # pylint: disable=relative-beyond-top-level


def get_user_by__id(db: Session, _id: int):
    user = db.query(models.User).filter(models.User.id == _id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with _id {_id} not found"
        )
    return user


def create_user(db: Session, request: schemas.User):
    new_user = models.User(
        name=request.name, email=request.email, password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
