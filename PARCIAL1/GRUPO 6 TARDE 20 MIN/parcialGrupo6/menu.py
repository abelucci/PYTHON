"""
Gestor de Gastos Personal - Archivo Principal
Sistema de control financiero personal con interfaz de consola
"""

# Importar módulos del sistema
from utils import mostrar_bienvenida
from archivos import cargar_datos, guardar_datos
from operaciones import (
    registrar_ingreso, registrar_gasto, ver_balance, 
    listar_movimientos, editar_movimiento, eliminar_movimiento, 
    borrar_todos_movimientos
)

# Variable global para almacenar movimientos
movimientos = []

def menu():
    """Muestra el menú principal del sistema"""
    print("\n" + "="*50)
    print("       🏠 MENÚ PRINCIPAL - GESTOR DE GASTOS")
    print("="*50)
    print("1. 💰 Registrar ingreso")
    print("2. 💸 Registrar gasto")
    print("3. 📊 Ver balance")
    print("4. 📋 Listar movimientos")
    print("5. ✏️  Editar movimiento")
    print("6. 🗑️  Eliminar movimiento")
    print("7. 🧹 Borrar todos los movimientos")
    print("8. 🚪 Salir")
    print("="*50)
    
    try:
        opcion = int(input("Selecciona una opción (1 a 8): "))
        return opcion
    except ValueError:
        print("Error: Por favor ingresa un número válido entre 1 y 8.")
        return None

def main():
    """Función principal del programa"""
    global movimientos
    
    # Cargar datos al iniciar el programa
    movimientos = cargar_datos()
    
    # Mostrar bienvenida
    mostrar_bienvenida()
    
    # Bucle principal del programa
    while True:
        opcion = menu()
        
        if opcion == 1:
            registrar_ingreso(movimientos)
        elif opcion == 2:
            registrar_gasto(movimientos)
        elif opcion == 3:
            ver_balance(movimientos)
        elif opcion == 4:
            listar_movimientos(movimientos)
        elif opcion == 5:
            editar_movimiento(movimientos)
        elif opcion == 6:
            eliminar_movimiento(movimientos)
        elif opcion == 7:
            borrar_todos_movimientos(movimientos)
        elif opcion == 8:
            guardar_datos(movimientos)
            print("Gestor finalizado, adios.")
            break
        else:
            print("Opción no válida. Por favor selecciona una opción entre 1 y 8.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
