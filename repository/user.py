from fastapi import HTTPException, status
from .. import models
from ..hashing import Hash
from sqlalchemy.orm import Session


def create(request, db:Session):
    user = models.User(email=request.email, name=request.name, password=Hash.bycrypt(request.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(id, db: Session):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User Not Found')
    return user

