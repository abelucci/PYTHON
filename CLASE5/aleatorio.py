try:
    # Abrimos el archivo en modo lectura
    archivo = open("archivos/texto.txt", "r")
    
    # Mostramos la posición inicial del cursor
    print("Posición inicial:", archivo.tell())
    
    # Movemos el cursor al 5º carácter
    archivo.seek(3)
    print("Desde la posición 3:", archivo.read()) # le puedo indicar cuantos caracteres puedo ver

except FileNotFoundError:
    print("No se encontró el archivo 'texto.txt'")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

finally:
    archivo.close()
    print("Archivo cerrado correctamente")