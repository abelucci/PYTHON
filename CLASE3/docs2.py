
def primera_letra_mayus(nombre):
    """
    Devuelve la primera letra del nombre en mayúscula.

    Parámetros:
        nombre (str): Nombre de la persona. Puede incluir espacios al inicio o final.

    Retorna:
        str: Primera letra del nombre en mayúscula. 
            Si el nombre está vacío, devuelve una cadena vacía.

    Ejemplo:
        >>> primera_letra_mayus(" juan")
        'J'
    """
    help(primera_letra_mayus)
    nombre = nombre.strip()  # elimina espacios al inicio y final
    if nombre:  # verificar que no esté vacío
        return nombre[0].upper()
    else:
        return ""

# Prueba
nombre = input("Ingrese su nombre: ")
print("Primera letra en mayúscula:", primera_letra_mayus(nombre))

