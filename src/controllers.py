from bson import ObjectId

from src.models.database import db
from src.models.model import TraineeModel, TraineeUpdateNodel

def helper_trainee(trainee) -> dict:
    return {
        "_id": str(trainee["_id"]),
        "document": str(trainee["_id"]),
        "firstname": trainee["firstname"],
        "lastname": trainee["lastname"],
        "age": trainee["age"],
        "email": trainee["email"],
        "program": trainee["program"],
        "record_number": trainee["record_number"],
    }