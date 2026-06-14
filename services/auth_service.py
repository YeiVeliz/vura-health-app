from utils.firebase_config import auth

class AuthService:
    @staticmethod
    def sign_in(email, password):
        """Inicia sesión con correo y contraseña."""
        return auth.sign_in_with_email_and_password(email, password)

    @staticmethod
    def sign_up(email, password):
        """Registra un nuevo usuario."""
        return auth.create_user_with_email_and_password(email, password)
