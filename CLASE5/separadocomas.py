import csv

try:
    archivo = open("archivos/datos.csv", "r")
    lector = csv.reader(archivo)

    for fila in lector:
        print(fila)

except FileNotFoundError:
    print("No se encontró el archivo 'datos.csv'")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

finally:
    archivo.close()
    print("Archivo cerrado correctamente")