from typing import List
from fastapi import APIRouter, Depends,status, HTTPException
from sqlalchemy.orm import Session
from database import connect
from . import schemas, models
from auth import services
from user import schemas as UserSchemas
import pickle
import numpy as np


router = APIRouter(
	prefix='/product',
	tags=['Product']
)

models.connect.Base.metadata.create_all(bind=connect.engine)

#open pickle file 
pickle_in = open("demand.pkl","rb")
model = pickle.load(pickle_in)


#return semua produk
@router.get("/",response_model=List[schemas.baseProduct])
def show_all(db:Session = Depends(connect.get_db),current_user:UserSchemas.User=Depends(services.get_current_user)):
        produk=db.query(models.Product).all()
        return produk

#create product
@router.post("/",status_code=status.HTTP_201_CREATED)
def add(request:schemas.product,db:Session=Depends(connect.get_db),current_user:UserSchemas.User=Depends(services.get_current_user)):
        newProd =models.Product(name=request.name,store_name=request.store_name,total_price=request.total_price,base_price=request.base_price) 
        db.add(newProd)
        db.commit()
        db.refresh(newProd)
        return newProd

#return product berdasarkan id
@router.get("/{id}",status_code=200,response_model=schemas.baseProduct)
def show(id,db:Session=Depends(connect.get_db),current_user:UserSchemas.User=Depends(services.get_current_user)):
        product=db.query(models.Product).filter(models.Product.product_id==id).first()
        if not product:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Product with the id {id} is not available")
        return product

#delete product
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete(id,db:Session=Depends(connect.get_db),current_user:UserSchemas.User=Depends(services.get_current_user)):
        db.query(models.Product).filter(models.Product.product_id==id).delete(synchronize_session=False)
        db.commit()
        return "Product Deleted"

#update product
@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.product,db:Session=Depends(connect.get_db),current_user:UserSchemas.User=Depends(services.get_current_user)):
        product=db.query(models.Product).filter(models.Product.product_id==id)
        if not product.first():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Product dengan id {id} tidak ditemukan")
        product.update(request.dict())
        db.commit()
        return 'Product Updated'


#prediksi permintaan konsumen
@router.post("/demand_prediction",response_model=schemas.prediction)
def predict_demand(request:schemas.parameter,db:Session=Depends(connect.get_db),current_user:UserSchemas.User=Depends(services.get_current_user)):
        total=request.price_total
        base=request.price_base
        array= np.array([[total,base]])
        prediction = model.predict(array)
        return{
                "prediction" : prediction
        }

        
