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
    return {"message": "Bienvenido a la API"}

# Registrar aprendices

@app.post(
    "/trainees/", response_description="Registrar un nuevo aprendiz", status_code=status.HTTP_201_CREATED,
)

def create_trainee_api(trainee: TraineeModel):
    # validar si ya existe el documento
    return create_trainee(trainee)

# Obtener la lista de aprendices
@app.get(
    "/trainees/", response_description="Listar todos los aprendices", status_code=status.HTTP_201_CREATED,
)
def get_all_trainee_api():
    return get_all_trainees()

# Obtener un aprendiz por su ID
@app.get(
    "/trainees/{id}", response_description="Obtener un aprendiz por su ID", status_code=status.HTTP_201_CREATED,
)

def get_trainee_by_id_api(id: str):
    trainee = get_trainee_by_id(id)
    if not trainee:
        raise HTTPException(status_code=404, detail="Aprendiz no encontrado")
    return trainee 

# Actualizar datos de un aprendiz por su ID
@app.put(
    "/trainees/{id}", response_description="Actualizar datos de un aprendiz por su ID",
)
def update_trainee_api(id: str, trainee: TraineeUpdateModel):
    trainee_updated = update_trainee(id, trainee)
    if not trainee_updated:
        raise HTTPException(status_code=404, detail="Aprendiz no encontrado")
    return trainee_updated

# Eliminar un aorendiz
@app.delete(
    "/trainees/{id}", response_description="Eliminar un aprendiz por su ID",
)

def delete_trainee_api(id: str):
    trainee = delete_trainee(id)
    if not trainee:
        raise HTTPException(status_code=404, detail="Aprendiz no encontrado")
    return {"mensaje": "Aprendiz eliminado correctamente"}