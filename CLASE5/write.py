try:
    archivo = open("archivos/saludo.txt", "w")
    archivo.write("Hola! Bienvenido a la uade.\n")
except IOError:
    print("Error: No se pudo escribir en el archivo.")
finally:
    archivo.close()