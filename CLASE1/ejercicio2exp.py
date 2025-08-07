negativos = 0
positivos = 0
numeroUsuario = -1 # se inicia en -1 solo para entrar al while. (No se cuenta este primer valor)

while (numeroUsuario != 0): #Se repite mientras el usuario NO ingrese el número 0.
                            #Si se escribe 0, se sale del bucle y pasa a mostrar los resultados.
    numeroUsuario = int(input("Ingrese un número: ")) #El número se convierte a entero con int() y se guarda en numeroUsuario.
    if (numeroUsuario > 0):
        positivos = positivos + 1 #Si el número ingresado es mayor que 0, se suma 1 al contador de positivos.
    if (numeroUsuario < 0):
        negativos = negativos + 1 #Si el número ingresado es menor que 0, se suma 1 al contador de negativos.
#Si el número es 0, no entra a ninguno de los if, y el bucle se termina.
print("Cantidad de positivos: ", positivos)
print("Cantidad de negativos: ", negativos)