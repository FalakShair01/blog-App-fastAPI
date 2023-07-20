from typing import List, Annotated
from fastapi import APIRouter, Depends,status, HTTPException, Response
from sqlalchemy.orm import Session
from .. import models, schemas, database, Oauth2
from ..repository import blog

router = APIRouter(
    prefix="/blogs",
    tags=['Blog']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.showBlog])
async def all_blogs(db: Session= Depends(get_db), get_current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return blog.get_all_blogs(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request:schemas.Blog, db: Session=Depends(get_db)):
    return blog.create(request=request, db=db)



@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.showBlog)
async def one_blog(id,response: Response, db:Session = Depends(get_db)):
    return blog.get_blog(db=db,id=id)


@router.delete('/{id}')
async def delete_blog(id: int, db: Session=Depends(get_db)):
    return blog.destroy(id=id,db=db)
    


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_blog(id:int, request: schemas.Blog, db: Session=Depends(get_db)):
    return blog.update_blog(id=id,db=db,request=request)