notas = [
    [7, 8, 5, 6],  # Alumno 1
    [1, 2, 5, 7],  # Alumno 2
    [8, 9, 10, 7], # Alumno 3
    [3, 3, 1, 6]   # Alumno 4
]

for i in range(len(notas)):
    promedio = sum(notas[i]) / len(notas[i])
    estado = "aprobado" if promedio >= 4 else "reprobado"
    print(f"Alumno {i+1} tiene un promedio de {promedio:.2f} y está {estado}.")
