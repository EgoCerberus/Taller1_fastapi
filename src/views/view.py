import requests

# URL limpia de la API de FastAPI
BASE_URL = "https://taller1-fastapi.onrender.com"
# BASE_URL = "http://127.0.0.1:8000"

def limpiar_pantalla():
    input("\nPresiona Enter para continuar...")
    print("\n" + "-" * 50 + "\n")
    
def mostrar_menu():
    print("\n==============================")
    print("  GESTIÓN DE APRENDICES - CLI")
    print("==============================")
    print("1. Registrar un nuevo aprendiz")
    print("2. Listar todos los aprendices")
    print("3. Buscar aprendiz por ID o Documento")
    print("4. Actualizar un aprendiz")
    print("5. Eliminar un aprendiz")
    print("6. Salir")
    
def registrar_aprendiz():
    print("\n--- REGISTRAR NUEVO APRENDIZ ---")
    document = input("Documento: ")
    firstname = input("Nombres: ")
    lastname = input("Apellidos: ")
    email = input("Correo electrónico: ")
    try:
        age = int(input("Edad: "))
    except ValueError:
        print("La edad debe ser un número entero.")
        return
    program = input("Programa de formación: ")
    try:
        record_number = int(input("Número de ficha: "))
    except ValueError:
        print("El número de ficha debe ser un entero.")
        return

    data = {
        "document": document,
        "firstname": firstname,
        "lastname": lastname,
        "email": email,
        "age": age,
        "program": program,
        "record_number": record_number
    }

    try:
        response = requests.post(f"{BASE_URL}/trainees/", json=data)
        if response.status_code == 201:
            print("\n¡Aprendiz registrado con éxito!")
            print(response.json())
        else:
            print(f"\nError al registrar ({response.status_code}): {response.text}")
    except requests.exceptions.RequestError as e:
        print(f"\nError de conexión con el servidor: {e}")

def listar_aprendices():
    try:
        response = requests.get(f"{BASE_URL}/trainees/")
        # Aceptamos tanto 200 como 201 por si la API aún retorna el status 201
        if response.status_code in [200, 201]:
            aprendices = response.json()
            if not aprendices:
                print("\nNo hay aprendices registrados.")
                return
            print("\n--- LISTA DE APRENDICES ---")
            for a in aprendices:
                print(f"ID: {a.get('id')} | Doc: {a.get('document')} | Nombre: {a.get('firstname')} {a.get('lastname')} | Programa: {a.get('program')}")
        else:
            print(f"\nError al obtener los datos: {response.text}")
    except requests.exceptions.RequestError as e:
        print(f"\nNo se pudo conectar con el servidor: {e}")

def buscar_aprendiz():
    trainee_id = input("\nIngrese el ID o Documento del aprendiz: ")
    try:
        response = requests.get(f"{BASE_URL}/trainees/{trainee_id}")
        if response.status_code == 200:
            a = response.json()
            print("\n--- DATOS DEL APRENDIZ ---")
            for k, v in a.items():
                print(f"{k}: {v}")
        else:
            print("\nAprendiz no encontrado.")
    except requests.exceptions.RequestError as e:
        print(f"\nError de conexión: {e}")

def actualizar_aprendiz():
    trainee_id = input("\nIngrese el ID del aprendiz a actualizar: ")
    print("Deje el espacio en blanco si no desea modificar un campo.")
    
    firstname = input("Nuevo nombre: ")
    lastname = input("Nuevo apellido: ")
    email = input("Nuevo correo: ")
    age_str = input("Nueva edad: ")
    program = input("Nuevo programa: ")
    record_str = input("Nuevo número de ficha: ")

    data = {}
    if firstname: data["firstname"] = firstname
    if lastname: data["lastname"] = lastname
    if email: data["email"] = email
    if age_str: data["age"] = int(age_str)
    if program: data["program"] = program
    if record_str: data["record_number"] = int(record_str)

    try:
        response = requests.put(f"{BASE_URL}/trainees/{trainee_id}", json=data)
        if response.status_code == 200:
            print("\n¡Aprendiz actualizado correctamente!")
            print(response.json())
        else:
            print(f"\nError al actualizar: {response.text}")
    except requests.exceptions.RequestError as e:
        print(f"\nError de conexión: {e}")

def eliminar_aprendiz():
    trainee_id = input("\nIngrese el ID del aprendiz a eliminar: ")
    confirmacion = input(f"¿Está seguro de eliminar al aprendiz {trainee_id}? (s/n): ")
    if confirmacion.lower() != 's':
        print("Operación cancelada.")
        return

    try:
        response = requests.delete(f"{BASE_URL}/trainees/{trainee_id}")
        if response.status_code == 200:
            print("\n¡Aprendiz eliminado exitosamente!")
        else:
            print("\nAprendiz no encontrado o error al eliminar.")
    except requests.exceptions.RequestError as e:
        print(f"\nError de conexión: {e}")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-6): ")
        if opcion == "1":
            registrar_aprendiz()
        elif opcion == "2":
            listar_aprendices()
        elif opcion == "3":
            buscar_aprendiz()
        elif opcion == "4":
            actualizar_aprendiz()
        elif opcion == "5":
            eliminar_aprendiz()
        elif opcion == "6":
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")
        limpiar_pantalla()

if __name__ == "__main__":
    main()