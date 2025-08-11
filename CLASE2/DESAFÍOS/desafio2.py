goles = [
    [2, 1, 3],  # Jugador 1
    [0, 2, 1],  # Jugador 2
    [1, 1, 1]   # Jugador 3
]

for i in range(len(goles)):
    suma_goles = sum(goles[i])
    print(f"Jugador {i+1} anotó un total de {suma_goles} goles.")
