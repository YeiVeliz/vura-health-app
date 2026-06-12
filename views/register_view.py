import flet as ft
from utils.firebase_config import auth

def RegisterView(page: ft.Page, navigate_to):
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
    
    confirm_password_input = ft.TextField(
        label="Confirmar Contraseña",
        password=True,
        can_reveal_password=True,
        width=300,
        border_radius=10,
        focused_border_color=ft.Colors.BLUE_700,
    )
    
    error_text = ft.Text(color=ft.Colors.RED_600, size=14, weight="bold")
    
    # Indicador de carga
    loading_indicator = ft.ProgressRing(visible=False, width=20, height=20, stroke_width=2)
    
    def handle_register(e):
        error_text.value = ""
        error_text.color = ft.Colors.RED_600
        loading_indicator.visible = True
        page.update()
        
        email = email_input.value.strip()
        password = password_input.value.strip()
        confirm_password = confirm_password_input.value.strip()
        
        if not email or not password or not confirm_password:
            error_text.value = "Por favor, completa todos los campos."
            loading_indicator.visible = False
            page.update()
            return
            
        if password != confirm_password:
            error_text.value = "Las contraseñas no coinciden."
            loading_indicator.visible = False
            page.update()
            return
            
        if len(password) < 6:
            error_text.value = "La contraseña debe tener al menos 6 caracteres."
            loading_indicator.visible = False
            page.update()
            return
            
        try:
            # Crear usuario en Firebase Auth
            user = auth.create_user_with_email_and_password(email, password)
            
            # Guardamos la sesión del usuario
            page.data = {"user": user}
            
            error_text.value = "¡Registro exitoso! Iniciando sesión..."
            error_text.color = ft.Colors.GREEN_600
            loading_indicator.visible = False
            page.update()
            
            # Navegar al Dashboard principal
            import time
            time.sleep(1)
            navigate_to("/home")
            
        except Exception as err:
            print("ERROR DETALLADO DE FIREBASE:", err)
            loading_indicator.visible = False
            # Mostramos el error real recortado para que quepa en pantalla
            error_text.value = f"Error: {str(err)[:30]}" 
            page.update()

    return ft.Container(
        content=ft.Column(
            [
                # Botón de retroceso
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
                ft.Icon(ft.Icons.PERSON_ADD_ROUNDED, size=80, color=ft.Colors.BLUE_700),
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                ft.Text("Registrarse", size=32, weight="bold", color=ft.Colors.BLUE_900),
                ft.Text("Únete a Vura para cuidar de tu salud", size=16, color=ft.Colors.BLUE_GREY_500),
                ft.Divider(height=30, color=ft.Colors.TRANSPARENT),
                email_input,
                password_input,
                confirm_password_input,
                error_text,
                loading_indicator,
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                ft.ElevatedButton(
                    "Crear Cuenta",
                    on_click=handle_register,
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
