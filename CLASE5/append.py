try:
    archivo = open("archivos/saludo.txt", "a")
    archivo.write("Hola! Bienvenido a la clase 1010.\n")
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    archivo.close()