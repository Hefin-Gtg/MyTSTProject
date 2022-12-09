from sqlalchemy import Column, Integer, String
from database import connect

class User(connect.Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True, index=True)
	username = Column(String, index=True)
	password = Column(String, index=True)
	email = Column(String, index=True, unique=True)

