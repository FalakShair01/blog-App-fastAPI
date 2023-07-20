from fastapi import HTTPException, status
from .. import models, schemas
from sqlalchemy.orm import Session


def get_all_blogs(db):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request, db):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_blog(db:Session,id):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'Error': f'No blog with the ID : {id}'}
    return blog

def destroy(id, db:Session):
    db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    db.commit()
    return {"Message": "Blog Deleted Successfully"}


def update_blog(id, db: Session, request:schemas.Blog):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog with This Id is not Found.")
    blog.update({'title': request.title, 'body': request.body})
    db.commit()

    return {"Successfully Updated."}