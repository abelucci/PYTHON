goles = [
    [2, 1, 3],  # Jugador 1
    [0, 2, 1],  # Jugador 2
    [1, 1, 1]   # Jugador 3
]

def calcular_totales(goles, total_general):
    for i in range(len(goles)):
        suma_goles = sum(goles[i])
        total_general += suma_goles
        print(f"Jugador {i+1} anotó un total de {suma_goles} goles.")
    return total_general  # devolvemos el total actualizado

# Variable definida afuera
total_general = 0

# Llamamos a la función y actualizamos
total_general = calcular_totales(goles, total_general)

print(f"\nCantidad total de goles entre todos los jugadores: {total_general}")
