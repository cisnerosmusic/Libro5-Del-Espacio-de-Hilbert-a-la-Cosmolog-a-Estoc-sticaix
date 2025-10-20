# 📦 utils/parameters.py

import json
import os

# Ruta por defecto del archivo de parámetros
DEFAULT_PATH = os.path.join("data", "params_default.json")

def load_params(path=DEFAULT_PATH):
    """Carga parámetros desde un archivo JSON."""
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"⚠️ Archivo no encontrado: {path}")
        return {}

def save_params(params, path=DEFAULT_PATH):
    """Guarda parámetros en un archivo JSON."""
    try:
        with open(path, 'w') as f:
            json.dump(params, f, indent=2)
        print(f"✅ Parámetros guardados en {path}")
    except Exception as e:
        print(f"❌ Error al guardar parámetros: {e}")

def update_param(params, key, value):
    """Actualiza un parámetro específico."""
    if key in params:
        print(f"🔧 Actualizando: {key} = {value}")
    else:
        print(f"➕ Añadiendo nuevo parámetro: {key} = {value}")
    params[key] = value
    return params

def print_params(params):
    """Imprime los parámetros en formato legible."""
    print("📋 Parámetros actuales:")
    for k, v in params.items():
        print(f" - {k}: {v}")
