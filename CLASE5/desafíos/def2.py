import csv

try:
    archivo = open("alumnos.csv", "r")
    lector = csv.DictReader(archivo)
    for fila in lector:
        try:
            print(f"Alumno: {fila['nombre']} | Nota: {fila['nota']}")
        except KeyError:
            print(f"Error: fila mal formada → {fila}")
except FileNotFoundError:
    print("Error: El archivo CSV no existe")
finally:
    archivo.close()