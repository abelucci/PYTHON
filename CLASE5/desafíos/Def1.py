try:
    archivo = open("saludo.txt", "w")
    archivo.write("Hola! Bienvenido a Python\n")
except IOError:
    print("Error al escribir en el archivo")
finally:
    archivo.close()

try:
    archivo = open("saludo.txt", "r")
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("Error: El archivo no existe")
finally:
    archivo.close()
