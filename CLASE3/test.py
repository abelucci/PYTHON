# Importo libreria que genera numeros aleatorios
import random as rd

# Funcion para crear el tablero
def crear_tablero(n):
    tablero = []
    for fila in range(n):
        tablero.append([]) 
        for columna in range(n):
            tablero[fila].append('_') 
    return tablero

 #Funcion para esconder el tesoro
def esconder_tesoro(tablero):
    n = len(tablero)
    fila_destino = rd.randint(0, (n - 1))
    columna_destino = rd.randint(0, (n - 1))

    tablero[fila_destino][columna_destino] = 'X'

# Funcion para mostrar el tablero
def mostrar_tablero(tablero):
    filas = len(tablero)
    columnas = len(tablero[0])
    for fila in range(filas):
        for columna in range(columnas):
            print(tablero[fila][columna], end=' ')
        print()  

# Funcion para empezar la busqueda del tesoro
def empezar_busqueda(tablero):
    n = len(tablero)
    intentos = 10

# Bucle para buscar el tesoro      
    tesoro_encontrado = False

    while not tesoro_encontrado and intentos > 0:
        fila_busqueda = -1 # 
        while fila_busqueda < 0 or fila_busqueda >= n:
            fila_busqueda = int(input(f'Ingrese la fila (0 a {n-1}): '))

        columna_busqueda = -1
        while columna_busqueda < 0 or columna_busqueda >= n:
            columna_busqueda = int(input(f'Ingrese la columna (0 a {n-1}): '))
        
# Verificación si el tesoro se encuentra en la posicion ingresada
        if tablero[fila_busqueda][columna_busqueda] is 'X':
           print("Felicidades encontraste el tesoro!!!")
           tesoro_encontrado = True 
        else:
            print(f"El tesoro no se encotraba en ese lugar, te quedan { intentos -1 } intentos")
            intentos -= 1
        
        if intentos == 0:
            print("No hay mas intentos, GAME OVER!")



# Programa principal
tablero = crear_tablero(3)
esconder_tesoro(tablero)
mostrar_tablero(tablero)
empezar_busqueda(tablero)