from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

# Crear una instancia del cliente en MongoDB y asignar un tiempo de espera para la seleccion del servidor
MONGO_URI = "mongodb+srv://andrescamilocordobaramirez978_db_user:Megustaelapex6@cluster0.jwsaac0.mongodb.net/?appName=Cluster0"
client = MongoClient(MONGO_URI)


# Crearla base de datos y la coleccion
db = client.dataap
collection = db.traine

try:
    # Intentar obtener información del servidor para verificar la conexión
    client.server_info()
    print("Conexión a MongoDB exitosa.")
    client.admin.command("ping")  # Verificar la conexión con un comando ping
except (ConnectionFailure, ServerSelectionTimeoutError) as e:
    print(f"Error al conectar a MongoDB: {e}")
finally:
    # Cerrar la conexión al final
    client.close()
