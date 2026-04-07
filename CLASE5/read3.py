try:
#Abrimos en modo solo lectura
    contenido = open("archivos/letras.txt", "r")

#Recorremos y mostramos cada línea, en el print viene incluido un \n, entonces por eso hay una separación
    for linea in contenido:
        print("Sin strip:", linea)
    print("------")
    contenido.seek(0)  # volver al inicio del archivo
    for linea in contenido:
        print("Con strip:", linea.strip()) #para quitar espacios en blanco o saltos de liena al principio o final del string

except FileNotFoundError:
    print("No existe el archivo")

finally:
    contenido.close()