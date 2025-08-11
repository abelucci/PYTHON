def mostrar_edad(nombre, edad): #agrego los parámetros que quiero trabajar, algo dinámico
    print(f"Hola, {nombre}, tenés, {edad}, años.")
    # usando f-string.
    # Dentro de las llaves {} va cualquier variable o expresión, 
    # y todo está "contenido" en un único string que empieza con f"...".
    # Una f-string (o formatted string) es una forma moderna y eficiente de incluir variables dentro de un texto en Python. 
    # Se introdujo en Python 3.6 y usa una letra f antes del string.

mostrar_edad("Lucas", 21)
mostrar_edad("Valentina", 18) 