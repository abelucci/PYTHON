def obtenerClaves(claveMaestra):
    """
    Separa la clave maestra en dos:
    - caja1: dígitos en posiciones pares
    - caja2: dígitos en posiciones impares
    """
    return claveMaestra[::2], claveMaestra[1::2]

#help(obtenerClaves)
# --- Programa principal ---
while True:
    claveMaestra = input("Ingrese la clave maestra (solo números, entre 6 y 8 dígitos): ")

    # Validaciones
    if not claveMaestra.isdigit():
        print("Error: La clave debe contener solo números.")
        continue
    if len(claveMaestra) < 6 or len(claveMaestra) > 8:
        print("Error: La clave debe tener entre 6 y 8 dígitos.")
        continue

    # Si pasó todas las validaciones, salimos del bucle
    break

# Obtener claves
caja1, caja2 = obtenerClaves(claveMaestra)

# Mostrar resultados
print(f"Clave válida ingresada.")
print(f"Clave caja 1: {caja1}")
print(f"Clave caja 2: {caja2}")
