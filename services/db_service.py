from utils.firebase_config import db

class DBService:
    @staticmethod
    def get_metrics(user_id):
        """Obtiene las métricas de salud de un usuario."""
        try:
            return db.child("users").child(user_id).child("metrics").get().val()
        except Exception as e:
            print(f"Error al obtener métricas: {e}")
            return None

    @staticmethod
    def save_metrics(user_id, metrics):
        """Guarda o actualiza las métricas de un usuario."""
        try:
            db.child("users").child(user_id).child("metrics").update(metrics)
            print("Métricas guardadas exitosamente.")
        except Exception as e:
            print(f"Error al guardar métricas: {e}")
