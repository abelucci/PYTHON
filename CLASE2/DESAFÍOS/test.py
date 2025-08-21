#Cantidad total de goles, pero en realidad es cantidad total por jugador, suponiendo que cada fila es un jugador
goles = [
    [2, 1, 0],
    [0, 3, 1],
    [1, 2, 2],
]


def total_goles(matriz):
    goles = 0
    for fila in matriz:
        for columna in fila:
            goles += columna

    print("Cantidad total de goles: ", goles)


total_goles(goles)