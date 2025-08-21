contador = 0
max_intentos = 5

while contador < max_intentos:
    texto = input("Escribe algo (0 para salir): ")
    if texto == "0":
        print("Saliendo del bucle...")
        break
    print(f"Ingresaste: {texto}")
    contador += 1

print("Fin del bucle")
