import pyrebase
import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Configuración de Firebase usando variables de entorno
config = {
    "apiKey": os.getenv("API_KEY"),
    "authDomain": os.getenv("AUTH_DOMAIN"),
    "projectId": os.getenv("PROJECT_ID"),
    "storageBucket": os.getenv("STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("MESSAGING_SENDER_ID"),
    "appId": os.getenv("APP_ID"),
    "databaseURL": os.getenv("DATABASE_URL")
}

# Inicialización
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
