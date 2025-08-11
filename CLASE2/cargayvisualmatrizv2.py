matrizAlumnos = []

cantidadAlumnos = int(input("¿Qué cantidad de alumnos desea cargar? "))

for fila in range(cantidadAlumnos):
    alumno = []
    print(f"Ingrese los datos del alumno  {fila + 1}")
    nombre = input("Nombre: ")
    legajo = input("Legajo: ")
    alumno.append(nombre)
    alumno.append(legajo)
    matrizAlumnos.append(alumno)

for fila in range(cantidadAlumnos):
    print(f"Datos del alumno {fila + 1}")
    print(f"Nombre: {matrizAlumnos[fila][0]}  Legajo: {matrizAlumnos[fila][1]}")