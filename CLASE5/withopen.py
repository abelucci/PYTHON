try:
    # Abrimos el archivo con with (se cierra automáticamente)
    with open("archivos/alumnos.txt", "r") as archivo:
        for linea in archivo:
            nombre, nota = linea.strip().split(",")
            print(f"Alumno: {nombre} | Nota: {nota}")
            
except FileNotFoundError:
    print("Error: El archivo no existe")
except IOError:
    print("Error: Problema al leer el archivo")
finally:
    print("Operación de lectura finalizada")