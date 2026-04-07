try:
#Abrimos en modo solo lectura
    contenido = open("archivos/letras.txt", "r")

#Recorremos y mostramos cada línea, en el print viene incluido un \n, entonces por eso hay una separación
    for linea in contenido:
        print(linea)

except FileNotFoundError:
    print("No existe el archivo")

finally:
    contenido.close()