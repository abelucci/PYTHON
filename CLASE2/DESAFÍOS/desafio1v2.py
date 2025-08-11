matriz_alumnos = [
    ["Lucas", "Valentina"],
    ["Juan", "María"],
    ["Ana", "Pedro"]
]

for fila in range(len(matriz_alumnos)): 
    for columna in range(len(matriz_alumnos[fila])):
            print(f"[{fila}][{columna}] -> {matriz_alumnos[fila][columna]}")