try:
#Abrimos en modo solo lectura
    contenido = open("archivos/letras.txt", "r")
#Recorremos todo el archivo de una sola vez como un único string gigante. Incluye todos los saltos de línea (\n).
#Consume más memoria, es poco recomendable en archivos muy grandes.
    lineas = contenido.read()
    print(lineas) # todo el contenido en un solo print.

except FileNotFoundError:
    print("No existe el archivo")

finally:
    contenido.close()