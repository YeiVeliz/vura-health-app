import pyrebase
import os
from dotenv import load_dotenv

load_dotenv()

required_env_vars = ["API_KEY", "AUTH_DOMAIN", "PROJECT_ID", "STORAGE_BUCKET", "MESSAGING_SENDER_ID", "APP_ID", "DATABASE_URL"]
for var in required_env_vars:
    if not os.getenv(var):
        raise Exception(f"Falta configurar la variable de entorno crítica: {var}. Por favor, verifica tu archivo .env.")

config = {
    "apiKey": os.getenv("API_KEY"),
    "authDomain": os.getenv("AUTH_DOMAIN"),
    "projectId": os.getenv("PROJECT_ID"),
    "storageBucket": os.getenv("STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("MESSAGING_SENDER_ID"),
    "appId": os.getenv("APP_ID"),
    "databaseURL": os.getenv("DATABASE_URL")
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
