from sqlalchemy import Column,Integer,String,Float,DateTime
from datetime import datetime
from app.db.base import Base

class Prediction(Base):
	__tablename__="predictions"
	id=Column(Integer,primary_key=True,index=True)
	input_data=Column(String,nullable=False)
	prediction=Column(Float,nullable=False)
	model_version=Column(String,nullable=False)
	timestamp=Column(DateTime,default=datetime.utcnow)