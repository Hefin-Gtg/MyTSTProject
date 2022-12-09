from pydantic import BaseModel

class product(BaseModel):
	name : str
	store_name : str
	total_price : float
	base_price : float 

class baseProduct(BaseModel):
    name:str
    store_name:str
    class Config():
        orm_mode=True

class parameter(BaseModel):
    price_total:float
    price_base:float

class prediction(BaseModel):
    prediction:int




