import json

try:
    # Abrimos el archivo
    archivo = open("archivos/datos.json", "r")
    
    # Cargamos el contenido JSON
    datos = json.load(archivo)
    
    # Recorremos la lista de usuarios
    for usuario in datos.get("usuarios", []):
        try:
            print(usuario["nombre"], usuario["edad"])
        except KeyError:
            print(f"Usuario mal formado: {usuario}")

except FileNotFoundError:
    print("No se encontró el archivo 'usuarios.json'")

except json.JSONDecodeError:
    print("Error al decodificar JSON")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

finally:
    archivo.close()
    print("Archivo cerrado correctamente")