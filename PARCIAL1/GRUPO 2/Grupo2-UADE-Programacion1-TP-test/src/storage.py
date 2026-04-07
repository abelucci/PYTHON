# storage.py - maneja la lectura y escritura de los csv - organizandolos en la carpeta data.
import csv
from pathlib import Path
from typing import List, Dict

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)


def poner_extension_csv(nombre: str) -> str:
    nombre = nombre.strip()
    if not nombre.lower().endswith(".csv"):
        nombre += ".csv"
    return nombre


def _ruta_data(nombre_o_ruta: str) -> Path:
    nombre = Path(nombre_o_ruta).name
    nombre = poner_extension_csv(nombre)
    return DATA_DIR / nombre


def crear_archivo_si_falta(ruta: str) -> None:
    p = _ruta_data(ruta)
    if not p.exists():
        with p.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f, fieldnames=["fecha", "desc", "cat", "monto", "moneda"])
            writer.writeheader()


def hay_archivo(ruta: str) -> bool:
    return _ruta_data(ruta).exists()


def cargar_gastos(ruta: str) -> List[Dict]:
    p = _ruta_data(ruta)
    gastos: List[Dict] = []
    if not p.exists():
        return gastos
    with p.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                fecha = row.get("fecha", "").strip()
                desc = row.get("desc", "").strip()
                cat = row.get("cat", "").strip()
                monto = row.get("monto", "").strip()
                moneda = row.get("moneda", "").strip().upper()
                gastos.append({"fecha": fecha, "desc": desc,
                              "cat": cat, "monto": monto, "moneda": moneda})
            except Exception:
                continue
    return gastos


def guardar_gastos(ruta: str, gastos: List[Dict]) -> None:
    p = _ruta_data(ruta)
    with p.open("w", newline="", encoding="utf-8") as f:
        fieldnames = ["fecha", "desc", "cat", "monto", "moneda"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for g in gastos:
            writer.writerow(g)
