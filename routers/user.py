from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from .. import database,models,schemas
from ..repository import user

router = APIRouter(
    prefix="/users",
    tags=['User']
)

get_db = database.get_db



@router.post('/', response_model=schemas.showUser)
async def create_user(request: schemas.User, db: Session=Depends(get_db)):
    return user.create(request=request, db=db)

@router.get('/{id}', response_model=schemas.showUser)
async def get_user(id:int, db: Session= Depends(get_db)):
    return user.get_user(id=id, db=db)

