def calcular_precio_final(precio): #agrego parámetros
    iva = precio * 0.21
    return precio + iva #retorno un valor

total = calcular_precio_final(1000) #agrego cualquier valor, solo es para calcular
print("El precio final es:", total)