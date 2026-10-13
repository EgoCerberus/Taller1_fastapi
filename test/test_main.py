from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

# pip install -r requirements.txt
# pip install pymongo

# Agrega la URI de conexión a tu base de datos MongoDB
MONGO_URI = "mongodb+srv://yeisonescobar572_db_user:FcIzioL7Oby1QxgJ@cluster0.teavs3j.mongodb.net/?appName=Cluster0"  # Cambia esto según tu configuración

# Crear instancia del cleinte de MongoDB con un tiempo de espera para la selección del servidor
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)  # Tiempo de espera de 3 segundos

# Crear la base de datos y la colección
db = client.amb703
collection = db.mesa

# Crear el modelo de datos para la colección
nueva_mesa = {
    "name": "Yeison Escobar",
    "status": "Alive",
    "species": "Human",
    "gender": "Male",
} 

# Insertar el modelo de datos en la colección
collection.insert_one(nueva_mesa)

try:
    # Intentar obtener información del servidor para verificar la conexión
    client.server_info()
    print("Conexión a MongoDB exitosa.")
    client.admin.command('ping')  # Verificar la conexión con un comando ping
except (ConnectionFailure, ServerSelectionTimeoutError) as e:
    print(f"Error al conectar a MongoDB: {e}")
finally:
    # Cerrar la conexión al final
    client.close()