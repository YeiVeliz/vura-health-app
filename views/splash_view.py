import flet as ft
import time
import threading
from services.auth_service import AuthService
from utils.styles import AppColors
from utils.session_manager import SessionManager
from utils.session_persistence import load_session
from utils import constants as fonts

class SplashView(ft.View):
    def __init__(self, page: ft.Page, navigate_to):
        super().__init__(route="/splash")
        self.page_ref = page
        self.navigate_to = navigate_to
        self.controls = [self._build_content()]
        # Lanzamos la lógica al inicializar la clase
        threading.Thread(target=self._check_session, daemon=True).start()

    def _build_content(self):
        return ft.Container(
            expand=True,
            gradient=ft.LinearGradient(
                begin=ft.Alignment(0, -1),
                end=ft.Alignment(0, 1),
                colors=[
                    "#002B36", 
                    "#14655B", 
                    "#55EFCB"
                ],
                stops=[0.0, 0.6, 1.0]
            ),
            
            content=ft.Column([
                ft.Container(expand=True),
                ft.Icon(ft.Icons.FAVORITE_ROUNDED, size=120, color=ft.Colors.WHITE),
                ft.Text(
                    "VURA",
                    font_family= fonts.FontsTitles.TITLE, 
                    size=50, 
                    color=ft.Colors.WHITE
                ),
                ft.Container(expand=True),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        )

    def _check_session(self):
        time.sleep(2) # Tiempo de Splash
        
        # Intentar restaurar sesión
        session_data = load_session()
        
        # En Flet, para actualizar desde un hilo secundario, 
        # basta con llamar a la función que navega y luego page.update()
        if session_data:
            try:
                # Intentar refrescar el token de Firebase
                user = AuthService.refresh_token(session_data['refreshToken'])
                SessionManager().set_user(user)
                # Navegación directa
                self.navigate_to("/home")
            except Exception:
                self.navigate_to("/welcome")
        else:
            self.navigate_to("/login")
