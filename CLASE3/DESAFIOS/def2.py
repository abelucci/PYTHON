def obtenerClaves(claveMaestra):
    return claveMaestra[::2], claveMaestra[1::2]
    
claveMaestra = "18293"

caja1, caja2 = obtenerClaves(claveMaestra)

print(f"Clave caja 1: {caja1}")
print(f"Clave caja 2: {caja2}")
