try:
    # Abrimos en modo agregar al final
    archivo = open("archivos/personas.txt", "a")

    nombre = " "
    while nombre != "":
        nombre = input("Ingrese un nombre (deje vacío para terminar): ")
        if nombre != "":
            print(nombre, file=archivo)  # print agrega salto de línea automáticamente

except Exception as e:
    print(f"Ocurrió un error al escribir el archivo: {e}")

finally:
    archivo.close()
    print("Archivo cerrado correctamente")
