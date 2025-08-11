# Inicializamos la matriz vacía
matriz_temperaturas = []

# Cantidad de ciudades
cantidad_ciudades = int(input("¿Cuántas ciudades desea registrar? "))

# Cantidad de días
cantidad_dias = int(input("¿Cuántos días quiere registrar la temperatura de cada ciudad? "))

# Carga manual de datos
for ciudad in range(cantidad_ciudades):
    nombre_ciudad = input(f"Ingrese el nombre de la ciudad {ciudad + 1}: ")
    temperaturas_ciudad = []
    
    for dia in range(cantidad_dias):
        temp = float(input(f"Ingrese la temperatura del Día {dia + 1} para {nombre_ciudad}: "))
        temperaturas_ciudad.append(temp)
    
    matriz_temperaturas.append([nombre_ciudad, temperaturas_ciudad])

# Mostrar datos
print("\n--- Registro de temperaturas ---")
for ciudad in matriz_temperaturas:
    nombre_ciudad = ciudad[0]
    temperaturas = ciudad[1]
    
    for dia, temp in enumerate(temperaturas, start=1):
        print(f"{nombre_ciudad} - Día {dia}: {temp} °C")
