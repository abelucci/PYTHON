nombres = ["Gabriela", "Pedro", "Juan"]
try:
    # Abrimos en modo escritura
    archivo = open("archivos/personas.txt", "w")
    
    # Recorremos la lista y agregamos cada nombre al archivo
    for nombre in nombres:
        archivo.write(nombre + "\n")

except Exception as e:
    print(f"Ocurrió un error al escribir el archivo: {e}")

finally:
    archivo.close()
    print("Archivo cerrado correctamente")