class SessionManager:
    _instance = None
    _user = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SessionManager, cls).__new__(cls)
        return cls._instance

    def set_user(self, user_data):
        """Guarda la información del usuario logueado."""
        self._user = user_data

    def get_user(self):
        """Retorna la información del usuario actual."""
        return self._user

    def clear_user(self):
        """Limpia la sesión al cerrar sesión."""
        self._user = None

    def is_logged_in(self):
        """Verifica si hay un usuario activo."""
        return self._user is not None
