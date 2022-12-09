from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import schemas,models
from auth import services
from database import connect


router=APIRouter(
    prefix="/user",
    tags=["users"]
)
models.connect.Base.metadata.create_all(bind=connect.engine)

get_db=connect.get_db

#create user
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.baseUser)
def create_user(request:schemas.User,db:Session=Depends(get_db)):  
        new_user=models.User(username=request.username,email=request.email,password=services.Hash.bcrypt(request.password)) 
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
 
#show user
@router.get("/",response_model=List[schemas.baseUser])
def getAll_user(db:Session=Depends(get_db)):
        user=db.query(models.User).all()
        return user