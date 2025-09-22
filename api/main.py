from fastapi import FastAPI
from database import Database
from models import Model
from services import ProcessService

app = FastAPI()
db = Database()
process_service = ProcessService()

@app.get("/")
async def root():
    return {"message": "gglib API is running!"}

@app.get("/api/models")
async def list_models():
    models = db.list()
    return{"models": [model.__dict__ for model in models]}

@app.post("api/models/{model_id}/serve")
async def serve_model(model_id: int):
    model=db.get_model_by_id(model_id)
    return {"status": "serving"}