import flet as ft

def WelcomeView(page: ft.Page, navigate_to):
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Vura", size=50, weight="bold", color=ft.Colors.BLUE_700),
                ft.Text("The Health App", size=20, color=ft.Colors.BLUE_GREY_500),
                ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
                ft.ElevatedButton(
                    "Iniciar Sesión",
                    on_click=lambda _: navigate_to("/login"),
                    width=250,
                    height=55,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                    )
                ),
                ft.Container(height=10), # Espaciador
                ft.OutlinedButton(
                    "Registrarse",
                    on_click=lambda _: navigate_to("/register"),
                    width=250,
                    height=55,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                    )
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.Alignment(0, 0),
        expand=True,
        padding=30,
    )
