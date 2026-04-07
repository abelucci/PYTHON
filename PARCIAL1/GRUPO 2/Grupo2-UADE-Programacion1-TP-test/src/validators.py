# validators.py - Contiene las validaciones para controlar los datos ingresados.
from datetime import datetime
from typing import Optional, Tuple
from models import CATEGORIAS


def convertir_fecha(s: str) -> Optional[datetime]:
    try:
        return datetime.strptime(s.strip(), "%Y-%m-%d")
    except ValueError:
        return None


def pedir_opcion(msg: str, minimo: int, maximo: int, input_fn=input) -> int:
    while True:
        s = input_fn(msg).strip()
        if s.isdigit():
            v = int(s)
            if minimo <= v <= maximo:
                return v
        print("Error: ingrese un número entre {} y {}.".format(minimo, maximo))


def pedir_fecha(msg: str, input_fn=input) -> str:
    while True:
        s = input_fn(msg).strip()
        if convertir_fecha(s):
            return s
        print("Error: formato de fecha inválido. Use YYYY-MM-DD.")


def pedir_texto(msg: str, minimo: int = 1, maximo: int = 120, input_fn=input) -> str:
    while True:
        s = input_fn(msg).strip()
        if minimo <= len(s) <= maximo:
            return s
        print("Error: el texto debe tener entre {} y {} caracteres.".format(
            minimo, maximo))


def pedir_categoria(msg: str, input_fn=input) -> str:
    print("Categorías:", ", ".join(CATEGORIAS))
    while True:
        s = input_fn(msg).strip()
        for c in CATEGORIAS:
            if s.lower() == c.lower():
                return c
        print("Error: categoría no válida. Ingrese una de la lista.")


def pedir_monto(msg: str, input_fn=input) -> float:
    while True:
        s = input_fn(msg).replace(",", ".").strip()
        try:
            v = float(s)
            if v > 0:
                return round(v, 2)
        except ValueError:
            pass
        print("Error: ingrese un número mayor a 0.")


def rango_fechas_esta_bien(desde: str, hasta: str) -> Tuple[bool, Optional[str]]:
    f_desde = convertir_fecha(desde)
    f_hasta = convertir_fecha(hasta)
    if not f_desde or not f_hasta:
        return False, "Fechas inválidas."
    if f_desde > f_hasta:
        return False, "La fecha 'Desde' no puede ser posterior a 'Hasta'."
    return True, None


def pedir_moneda(msg: str, input_fn=input) -> str:
    while True:
        s = input_fn(msg).strip().upper()
        if s in ("ARS", "USD"):
            return s
        print("Error: ingrese ARS o USD.")
