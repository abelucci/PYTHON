negativos = 0
positivos = 0
numeroUsuario = -1 

while (numeroUsuario != 0):
    numeroUsuario = int(input("Ingrese un número: "))
    if (numeroUsuario > 0):
        positivos = positivos + 1
    if (numeroUsuario < 0):
        negativos = negativos + 1

print("Cantidad de positivos: ", positivos)
print("Cantidad de negativos: ", negativos)