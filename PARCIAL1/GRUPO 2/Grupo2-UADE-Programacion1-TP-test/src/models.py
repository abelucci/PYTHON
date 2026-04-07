# models.py - define la estructura de datos.
from pathlib import Path

ARCHIVO_DEFECTO = "gastos.csv"
CATEGORIAS = ["Comida", "Transporte", "Hogar",
              "Servicios", "Ocio", "Salud", "Educación"]

BASE_DIR = Path(__file__).resolve().parent.parent
