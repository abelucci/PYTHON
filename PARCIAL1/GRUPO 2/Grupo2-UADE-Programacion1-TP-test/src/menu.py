# menu.py - Controla lo que hace el usuario con el programa
from typing import List, Dict, Callable
from validators import pedir_opcion, pedir_fecha, pedir_texto, pedir_categoria, pedir_monto, pedir_moneda, rango_fechas_esta_bien
from services import (
    agregar_gasto, listar_gastos, listar_por_categoria,
    totales_por_categoria, totales_por_rango,
    matriz_mensual, armar_tabla, armar_matriz, armar_totales_por_moneda
)


def mostrar_menu() -> None:
    print("\n=== Sistema de Gestión de Gastos ===")
    print("1) Registrar gasto")
    print("2) Listar todos los gastos")
    print("3) Listar gastos por categoría")
    print("4) Ver total por categoría (separado por moneda)")
    print("5) Ver total por rango de fechas (separado por moneda)")
    print("6) Resumen mensual por categoría (matriz)")
    print("7) Guardar datos")
    print("0) Salir")


def pausar():
    input("\nPresione Enter para volver al menú...")


def bucle_principal(gastos: List[Dict], al_guardar: Callable[[List[Dict]], None]) -> None:
    op = -1
    while op != 0:
        mostrar_menu()
        op = pedir_opcion("Seleccione una opción: ", 0, 7)
        if op == 1:
            print("\nRegistrar gasto")
            fecha = pedir_fecha("Fecha (YYYY-MM-DD): ")
            desc = pedir_texto("Descripción: ")
            cat = pedir_categoria("Categoría: ")
            monto = pedir_monto("Monto: ")
            moneda = pedir_moneda("Moneda (ARS/USD): ")
            agregar_gasto(gastos, fecha, desc, cat, monto, moneda)
            print("✔ Gasto registrado correctamente.")
            pausar()
        elif op == 2:
            print("\nListado de gastos")
            print(armar_tabla(listar_gastos(gastos)))
            pausar()
        elif op == 3:
            print("\nListado por categoría")
            cat = pedir_categoria("Ingrese categoría: ")
            print(armar_tabla(listar_por_categoria(gastos, cat)))
            pausar()
        elif op == 4:
            cat = pedir_categoria("\nIngrese categoría: ")
            totales = totales_por_categoria(gastos, cat)
            print(armar_totales_por_moneda(f"Total en {cat}", totales))
            pausar()
        elif op == 5:
            print("\nTotal por rango de fechas")
            desde = pedir_fecha("Desde (YYYY-MM-DD): ")
            hasta = pedir_fecha("Hasta (YYYY-MM-DD): ")
            ok, msg = rango_fechas_esta_bien(desde, hasta)
            if not ok:
                print("Error:", msg)
            else:
                totales = totales_por_rango(gastos, desde, hasta)
                print(armar_totales_por_moneda(
                    f"Total de {desde} a {hasta}", totales))
            pausar()
        elif op == 6:
            print("\nResumen mensual por categoría (MATRIZ)")
            cats, meses, matriz = matriz_mensual(gastos)
            print(armar_matriz(cats, meses, matriz))
            print("\n* Nota: la matriz suma montos sin conversión de moneda.")
            pausar()
        elif op == 7:
            al_guardar(gastos)
            print("Datos guardados.")
            pausar()
        else:
            al_guardar(gastos)
            print("Programa finalizado.")
