import flet as ft

def WelcomeView(page: ft.Page, navigate_to):
    return ft.Container(
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=[ft.Colors.BLUE_900, ft.Colors.BLUE_500],
        ),
        content=ft.Column(
            [
                ft.Container(height=100),
                ft.Icon(ft.Icons.FAVORITE_ROUNDED, size=120, color=ft.Colors.WHITE30),
                ft.Text("VURA", size=45, weight="bold", color=ft.Colors.WHITE),
                ft.Text("tu aplicación de confianza\npara gestionar tu salud", 
                        size=16, color=ft.Colors.WHITE70, text_align=ft.TextAlign.CENTER),
                ft.Container(expand=True),
                ft.ElevatedButton(
                    "Sign In",
                    on_click=lambda _: navigate_to("/login"),
                    width=300, height=50,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=20),
                        bgcolor=ft.Colors.WHITE,
                        color=ft.Colors.BLUE_900,
                    )
                ),
                ft.Container(height=10),
                ft.OutlinedButton(
                    "Sign up",
                    on_click=lambda _: navigate_to("/register"),
                    width=300, height=50,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=20),
                        side=ft.BorderSide(1, ft.Colors.WHITE),
                        color=ft.Colors.WHITE,
                    )
                ),
                ft.Container(height=50),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20,
        expand=True,
    )
