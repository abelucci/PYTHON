# Matriz ya cargada
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

# Recorrer y mostrar cada elemento con sus coordenadas
for i in range(len(matriz)):         # Filas
    for j in range(len(matriz[i])):  # Columnas
        print(f"[{i}][{j}] -> {matriz[i][j]}")
