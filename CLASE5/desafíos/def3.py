import json

try:
    archivo = open("usuarios.json", "r")
    datos = json.load(archivo)
    for usuario in datos.get("usuarios", []):
        try:
            print(f"Nombre: {usuario['nombre']}, Edad: {usuario['edad']}")
        except KeyError:
            print(f"Error: datos incompletos → {usuario}")
except FileNotFoundError:
    print("Error: El archivo JSON no existe")
except json.JSONDecodeError:
    print("Error: El archivo JSON está mal formado")
finally:
    archivo.close()