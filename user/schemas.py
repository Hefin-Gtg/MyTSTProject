from pydantic import BaseModel

class User(BaseModel):
	username:str
	password:str
	email:str

class baseUser(User):
	username:str
	email:str

	class Config:
		orm_mode = True

class CreateUser(User):
	pass

	class Config:
		orm_mode = True

# Get user
class GetUser(BaseModel):
	username:str
	email:str

	class Config:
		orm_mode = True
