import flet as ft
from utils.firebase_config import auth

def LoginView(page: ft.Page, navigate_to):
    email_input = ft.TextField(
        label="Correo electrónico",
        keyboard_type=ft.KeyboardType.EMAIL,
        width=300,
        border_radius=10,
        focused_border_color=ft.Colors.BLUE_700,
    )
    
    password_input = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=300,
        border_radius=10,
        focused_border_color=ft.Colors.BLUE_700,
    )
    
    error_text = ft.Text(color=ft.Colors.RED_600, size=14, weight="bold")
    
    # Indicador de carga
    loading_indicator = ft.ProgressRing(visible=False, width=20, height=20, stroke_width=2)
    
    def handle_login(e):
        error_text.value = ""
        error_text.color = ft.Colors.RED_600
        loading_indicator.visible = True
        page.update()
        
        email = email_input.value.strip()
        password = password_input.value.strip()
        
        if not email or not password:
            error_text.value = "Por favor, completa todos los campos."
            loading_indicator.visible = False
            page.update()
            return
            
        try:
            # Intentar iniciar sesión con Firebase
            user = auth.sign_in_with_email_and_password(email, password)
            
            # Guardamos la sesión del usuario en la página
            page.data = {"user": user}
            
            error_text.value = "¡Inicio de sesión exitoso!"
            error_text.color = ft.Colors.GREEN_600
            loading_indicator.visible = False
            page.update()
            
            # Navegar al Dashboard principal
            import time
            time.sleep(1)
            navigate_to("/home")
            
        except Exception as err:
            print("Error en login:", err)
            loading_indicator.visible = False
            error_text.value = "Correo o contraseña incorrectos."
            page.update()

    return ft.Container(
        content=ft.Column(
            [
                # Botón de retroceso alineado a la izquierda
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK_IOS_NEW,
                            on_click=lambda _: navigate_to("/"),
                            icon_color=ft.Colors.BLUE_700,
                            icon_size=20,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                ft.Icon(ft.Icons.LOCK_PERSON_ROUNDED, size=80, color=ft.Colors.BLUE_700),
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                ft.Text("Iniciar Sesión", size=32, weight="bold", color=ft.Colors.BLUE_900),
                ft.Text("Bienvenido de vuelta a Vura", size=16, color=ft.Colors.BLUE_GREY_500),
                ft.Divider(height=30, color=ft.Colors.TRANSPARENT),
                email_input,
                password_input,
                error_text,
                loading_indicator,
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                ft.ElevatedButton(
                    "Entrar",
                    on_click=handle_login,
                    width=300,
                    height=55,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=12),
                        bgcolor=ft.Colors.BLUE_700,
                        color=ft.Colors.WHITE,
                    )
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.Alignment(0, 0),
        expand=True,
        padding=20,
    )
