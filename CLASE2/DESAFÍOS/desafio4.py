# Definir la matriz vacía
matriz_temperaturas = []

# Pedir cantidad de ciudades
cantidad_ciudades = int(input("¿Cuántas ciudades desea registrar? "))

# Cargar manualmente la matriz
for ciudad in range(cantidad_ciudades):
    fila_temperaturas = []
    print(f"\nCiudad {ciudad + 1}:")
    for dia in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
        fila_temperaturas.append(temperatura)
    matriz_temperaturas.append(fila_temperaturas)

# Mostrar la matriz con índices
print("\n--- Registro de temperaturas ---")
for fila in range(len(matriz_temperaturas)):
    for columna in range(len(matriz_temperaturas[fila])):
        print(f"[{fila}][{columna}] -> {matriz_temperaturas[fila][columna]}")
