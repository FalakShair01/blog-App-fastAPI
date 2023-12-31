from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas,database,models
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm
from ..token import create_access_token

router = APIRouter(
    tags=['Authentication']
    )


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db:Session= Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credientials")
    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Password")

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}