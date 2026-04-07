# services.py - Logica del programa
from typing import List, Dict, Tuple
from validators import convertir_fecha
from models import CATEGORIAS


def agregar_gasto(gastos: List[Dict], fecha: str, desc: str, cat: str, monto: float, moneda: str) -> None:
    gastos.append({"fecha": fecha, "desc": desc, "cat": cat,
                  "monto": monto, "moneda": moneda})


def listar_gastos(gastos: List[Dict]) -> List[Dict]:
    return sorted(gastos, key=lambda x: x.get("fecha", ""))


def listar_por_categoria(gastos: List[Dict], cat: str) -> List[Dict]:
    cat_min = (cat or "").lower()
    return sorted([g for g in gastos if (g.get("cat") or "").lower() == cat_min], key=lambda x: x.get("fecha", ""))

# -------- Totales separados por moneda --------


def _sumar_por_moneda(items: List[Dict]) -> Dict[str, float]:
    tot = {}  # e.g., {'ARS': 12345.0, 'USD': 99.0}
    for g in items:
        mon = (g.get("moneda") or "ARS").upper()
        try:
            val = float(g.get("monto", 0) or 0)
        except (TypeError, ValueError):
            val = 0.0
        tot[mon] = round(tot.get(mon, 0.0) + val, 2)
    return tot


def totales_por_categoria(gastos: List[Dict], cat: str) -> Dict[str, float]:
    cat_min = (cat or "").lower()
    filtrados = [g for g in gastos if (g.get("cat") or "").lower() == cat_min]
    return _sumar_por_moneda(filtrados)


def totales_por_rango(gastos: List[Dict], desde: str, hasta: str) -> Dict[str, float]:
    f_desde = convertir_fecha(desde)
    f_hasta = convertir_fecha(hasta)
    if not f_desde or not f_hasta:
        return {}
    filtrados: List[Dict] = []
    for g in gastos:
        f = convertir_fecha(g.get("fecha", ""))
        if f and f_desde <= f <= f_hasta:
            filtrados.append(g)
    return _sumar_por_moneda(filtrados)

# -------- Matriz categoría × mes (sin conversión de moneda) --------


def matriz_mensual(gastos: List[Dict], anio=None) -> Tuple[List[str], List[str], List[List[float]]]:
    cats = CATEGORIAS[:]
    meses = [str(m) for m in range(1, 13)]
    matriz = [[0.0 for _ in range(12)] for _ in cats]
    if not gastos:
        return cats, meses, matriz

    if anio is None:
        anio = 0
        for g in sorted(gastos, key=lambda x: x.get("fecha", "")):
            f = convertir_fecha(g.get("fecha", ""))
            if f:
                anio = f.year
                break

    idx_cat = {c: i for i, c in enumerate(cats)}
    for g in gastos:
        f = convertir_fecha(g.get("fecha", ""))
        if not f:
            continue
        if anio != 0 and f.year != anio:
            continue
        # normalizar categoría
        crudo = g.get("cat", "")
        cat_norm = None
        for c in cats:
            if c.lower() == crudo.lower():
                cat_norm = c
                break
        if cat_norm is None:
            continue
        # sumar monto (sin convertir moneda)
        try:
            monto = float(g.get("monto", 0) or 0)
        except (TypeError, ValueError):
            monto = 0.0
        i = idx_cat[cat_norm]
        j = f.month - 1
        matriz[i][j] += monto

    for i in range(len(matriz)):
        matriz[i] = [round(x, 2) for x in matriz[i]]
    return cats, meses, matriz

# -------- Salidas formateadas --------


def armar_tabla(gastos: List[Dict]) -> str:
    if not gastos:
        return "No hay registros para mostrar."
    out = [
        "------------------------------------------------------",
        "# | Fecha      | Descripción                  | Categoría   | Monto     | Moneda",
        "------------------------------------------------------"
    ]
    for i, g in enumerate(gastos, start=1):
        fecha = g.get("fecha", "")
        desc = g.get("desc", "")
        cat = g.get("cat", "")
        mon = (g.get("moneda", "ARS") or "ARS").upper()
        try:
            monto = float(g.get("monto", 0) or 0)
        except (TypeError, ValueError):
            monto = 0.0
        desc_corta = (desc[:22] + "…") if len(desc) > 23 else desc
        out.append("{:>2} | {} | {:<23} | {:<11} | ${:<8.2f} | {}".format(
            i, fecha, desc_corta, cat, monto, mon))
    out.append("------------------------------------------------------")
    out.append("Total de registros: {}".format(len(gastos)))
    return "\n".join(out)


def armar_matriz(cats: List[str], meses: List[str], matriz: List[List[float]]) -> str:
    ancho = 10
    header = "Categoría".ljust(12) + "".join(m.rjust(ancho) for m in meses)
    lineas = [header, "-" * (12 + len(meses) * ancho)]
    for c, fila in zip(cats, matriz):
        linea = c.ljust(
            12) + "".join("{:.2f}".rjust(ancho).format(v) for v in fila)
        lineas.append(linea)
    return "\n".join(lineas)


def armar_totales_por_moneda(titulo: str, totales: Dict[str, float]) -> str:
    if not totales:
        return f"{titulo}: sin datos."
    lineas = [titulo + ":"]
    for mon, val in totales.items():
        lineas.append(f"  - {mon}: ${val:.2f}")
    return "\n".join(lineas)
