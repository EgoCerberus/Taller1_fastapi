from src.templates.controllers import create_trainee, get_all_trainees, get_trainee_by_id, update_trainee, delete_trainee

from src.models.model import TraineeModel, TraineeUpdateModel
from fastapi import FastAPI, HTTPException, status

# uvicorn src.main:app --reload
app = FastAPI(
    title="Gestion de datos de los aprendices", 
    description="API simple con FastAPI para la gestión de datos de los aprendices",
    version="1.0.0",
)
@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de gestión de datos de los aprendices"}