nombres = ["Gabriela", "Oliver", "Juan"]

try:
    # Abrimos en modo escritura
    archivo = open("archivos/personas.txt", "w")
    
    # Escribimos cada nombre usando print
    for nombre in nombres:
        print(nombre, file=archivo)  # print agrega automáticamente salto de línea

except Exception as e:
    print(f"Ocurrió un error al escribir el archivo: {e}")

finally:
    archivo.close()
    print("Archivo cerrado correctamente")