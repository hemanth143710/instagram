from http.client import HTTPException
from sqlalchemy.orm import Session
from routers.schemas import PostBase
from fastapi import APIRouter, Depends, status
from db.database import get_db
from db import db_post

router = APIRouter(
    prefix='/post',
    tags=['post']
)
image_url_types =['absolute','relative']

@router.post('')
def create(request: PostBase,db:Session = Depends(get_db)):
    if not request.image_url_type in image_url_types:
        return ('unprosible')
    return db_post.create