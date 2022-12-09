from sqlalchemy import Column, Integer, String, Float
from database import connect


class Product(connect.Base):
	__tablename__ = 'product'

	product_id = Column(Integer, primary_key=True, index=True)
	name = Column(String)
	store_name = Column(String)
	total_price = Column(Float)
	base_price = Column(Float)
	demand = Column(Float)
