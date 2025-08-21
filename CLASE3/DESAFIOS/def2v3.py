def obtenerClaves(claveMaestra):
    """
    Separa la clave maestra en dos claves:
    - Caja 1: dígitos en posiciones pares.
    - Caja 2: dígitos en posiciones impares.
    """
    return claveMaestra[::2], claveMaestra[1::2]


# Parámetros de validación
min_len = 6
max_len = 8

# Pedir la clave al usuario con máximo 3 intentos
for intento in range(3):
    claveMaestra = input("Ingrese la clave maestra (solo números, tres intentos, minímo 6, máx 8): ")

    if claveMaestra.isdigit() and min_len <= len(claveMaestra) <= max_len:
        caja1, caja2 = obtenerClaves(claveMaestra)
        print(f"Clave caja 1: {caja1}")
        print(f"Clave caja 2: {caja2}")
        break  # Sale del bucle porque ya es válido
    else:
        print(f"Clave inválida. Debe ser numérica y tener entre {min_len} y {max_len} dígitos.")
else:
    # Este else se ejecuta si el for termina sin un break
    print("Demasiados intentos fallidos. Acceso denegado.")
