import json
import os

SESSION_FILE = "session.json"

def save_session(user_data):
    """Guarda el token de refresco en un archivo local."""
    with open(SESSION_FILE, "w") as f:
        json.dump(user_data, f)

def load_session():
    """Carga el token de refresco desde un archivo local."""
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "r") as f:
            return json.load(f)
    return None

def clear_session():
    """Borra el archivo de sesión al cerrar sesión."""
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
