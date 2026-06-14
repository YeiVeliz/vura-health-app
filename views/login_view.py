import flet as ft
import time
from services.auth_service import AuthService
from utils.styles import AppStyles
from utils.session_manager import SessionManager
from utils import constants as fonts

class LoginView(ft.View):
    def __init__(self, page: ft.Page, navigate_to):
        super().__init__(route="/login")
        self.page_ref = page
        self.navigate_to = navigate_to
        self.input_style = AppStyles.INPUT_STYLE
        self.controls = [self._build_content()]

    def _build_content(self):
        def create_input(label, hint, password=False):
            return ft.Column([
                ft.Text(
                    label, 
                    size=12, 
                    weight="w600",
                    color="#002B36",
                    font_family=fonts.FontsApp.NORMAL
                ),
                ft.TextField(
                    hint_text=hint, 
                    password=password, 
                    can_reveal_password=password, 
                    **{
                        **self.input_style, 
                        "text_style": ft.TextStyle(font_family=fonts.FontsApp.LIGHT, size=10),
                        "hint_style": ft.TextStyle(font_family=fonts.FontsApp.LIGHT, color=ft.Colors.GREY_500, size=10)
                    }
                )
            ], spacing=5)

        email = create_input("Correo Electrónico", "ejemplo@correo.com")
        password = create_input("Contraseña", "********", password=True)
        
        container = ft.Container(
            expand=True,
            gradient=ft.LinearGradient(
                begin=ft.Alignment(0, -1),
                end=ft.Alignment(0, 1),
                colors=["#002B36", "#14655B", "#A7FFEB"],
                stops=[0.0, 0.6, 1.0]
            ),
            content=ft.Column([
                ft.Container(height=40),
                ft.Row([ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: self.navigate_to("/"), icon_color=ft.Colors.WHITE)]),
                ft.Container(height=10),
                ft.Container(
                    alignment=ft.Alignment.CENTER,
                    content=ft.Text(
                        "Bienvenido de nuevo", 
                        size=25, 
                        color=ft.Colors.WHITE, 
                        font_family=fonts.FontsTitles.TITLE
                    ),
                ),
                ft.Container(height=10),
                ft.Container(
                    bgcolor=ft.Colors.WHITE,
                    border_radius=ft.BorderRadius(40, 40, 0, 0),
                    padding=30,
                    expand=True,
                    content=ft.Column([
                        ft.Container(height=10),
                        email,
                        ft.Container(height=10),
                        password,
                        ft.Container(height=5),
                        ft.Row([ft.TextButton("¿Olvidaste tu contraseña?", on_click=lambda _: None, style=ft.ButtonStyle(color="#14655B"))], alignment=ft.MainAxisAlignment.END),
                        ft.Container(height=15),
                        ft.ElevatedButton(
                            content=ft.Text("Inicia Sesión", font_family=fonts.FontsApp.BOLD, color=ft.Colors.WHITE),
                            on_click=lambda e: self.handle_login(email.controls[1].value, password.controls[1].value),
                            width=float("inf"), 
                            height=50, 
                            style=AppStyles.get_elevated_button_style(bgcolor="#14655B")
                        ),
                        ft.Container(height=10),
                        ft.Divider(color=ft.Colors.GREY_300),
                        ft.Container(height=10),
                        ft.Row([
                            ft.IconButton(ft.Icons.FACEBOOK, icon_color=ft.Colors.BLUE_800, icon_size=40), 
                            ft.IconButton(ft.Icons.G_MOBILEDATA, icon_color=ft.Colors.RED_600, icon_size=40), 
                            ft.IconButton(ft.Icons.APPLE, icon_color=ft.Colors.BLACK, icon_size=40)
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                        ft.Container(expand=True),
                        ft.Row([ft.Text("¿No tienes cuenta?"), ft.TextButton("Crea una", on_click=lambda _: self.navigate_to("/register"), style=ft.ButtonStyle(color="#14655B"))], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Container(height=10)
                    ], spacing=10)
                )
            ], spacing=0)
        )
        
        # Animación
        container.opacity = 0
        container.animate_opacity = 500
        
        async def animate_in():
            time.sleep(0.05)
            container.opacity = 1
            container.update()
        
        self.page_ref.run_task(animate_in)
        
        return container

    def handle_login(self, email, password):
        try:
            user = AuthService.sign_in(email, password)
            SessionManager().set_user(user)
            self.navigate_to("/home")
        except Exception as e:
            print(f"Error login: {e}")
