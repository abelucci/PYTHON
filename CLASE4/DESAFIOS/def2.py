nombres = ["Ana", "Juan", "Pedro"]

indice = int(input("Ingresá un índice: "))

try:
    print("Nombre:", nombres[indice])
except IndexError:
    print("Error: índice fuera de rango")