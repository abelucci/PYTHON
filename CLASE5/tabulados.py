try:
    # Abrimos el archivo en modo lectura
    archivo = open("archivos/datos.tsv", "r")

    # Leemos cada línea y separamos por tabulador
    for linea in archivo:
        nombre, edad = linea.strip().split("\t")
        print(nombre, edad)
        
except FileNotFoundError:
    print("No se encontró el archivo 'datos.tsv'")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

finally:
    archivo.close()
    print("Archivo cerrado correctamente")