matriz = []  # Matriz vacía

for i in range(2):  # 2 Filas
    fila = []
    for j in range(3):  # 3 Columnas
        valor = input(f"Ingrese valor para posición [{i}][{j}]: ")
        fila.append(valor)
    matriz.append(fila)

print("\nMatriz cargada:")
for fila in matriz:
    print(fila)
