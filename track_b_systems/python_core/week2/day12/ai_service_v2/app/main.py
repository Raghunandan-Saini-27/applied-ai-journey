from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.db import models			#Important : Ensure models are registered

app=FastAPI()

@app.on_event("startup")
def on_startup():
	Base.metadata.create_all(bind=engine)

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working"}