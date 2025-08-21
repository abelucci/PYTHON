# Pedimos el valor y convertimos a int
valor = int(input("Ingrese un valor: "))

def cubo(x):
    """Eleva al cubo el parámetro recibido"""
    return x**3

# Mostrar ayuda de la función
help(cubo)

# Calcular el cubo y mostrarlo
resultado = cubo(valor)
print(f"El cubo de {valor} es {resultado}")
