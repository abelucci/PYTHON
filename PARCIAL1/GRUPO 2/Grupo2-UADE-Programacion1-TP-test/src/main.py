# main.py - Controla el programa
from typing import List, Dict, Optional
from storage import cargar_gastos, guardar_gastos, crear_archivo_si_falta, poner_extension_csv, hay_archivo
from validators import pedir_opcion, pedir_texto
from menu import bucle_principal


def elegir_csv() -> Optional[str]:
    print("==============================================")
    print(" Bienvenido al Sistema de Gestión de Gastos ")
    print("==============================================")
    print("1) Elegir un CSV existente con gastos")
    print("2) Crear un CSV nuevo")
    print("3) Salir")
    op = pedir_opcion("Seleccione una opción: ", 1, 3)

    if op == 1:
        nombre = pedir_texto("Ruta/nombre del CSV existente: ")
        nombre = poner_extension_csv(nombre)
        if not hay_archivo(nombre):
            print("No se encontró ese archivo.")
            return None
        return nombre

    if op == 2:
        nombre = pedir_texto("Nombre del CSV nuevo: ")
        nombre = poner_extension_csv(nombre)
        crear_archivo_si_falta(nombre)
        print("Archivo creado:", nombre)
        return nombre

    print("Saliendo del programa.")
    return None


def main() -> None:
    ruta_csv = elegir_csv()
    if ruta_csv is None:
        return

    gastos: List[Dict] = cargar_gastos(ruta_csv)

    def cuando_guardo(g: List[Dict]) -> None:
        guardar_gastos(ruta_csv, g)

    bucle_principal(gastos, cuando_guardo)


if __name__ == "__main__":
    main()
