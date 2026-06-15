import flet as ft
from utils import constants as fonts

class WelcomeView(ft.View):
    def __init__(self, page: ft.Page, navigate_to):
        super().__init__(route="/welcome")
        self.page_ref = page
        self.navigate_to = navigate_to
        self.controls = [self._build_content()]

    def _build_content(self):
        return ft.Container(
            gradient= ft.LinearGradient(
                begin=ft.Alignment.TOP_CENTER,
                end=ft.Alignment.BOTTOM_CENTER,
                colors=[
                    "#002B36", 
                    "#14655B",
                    "#55EFCB"
                    ],
                    stops = [0.0, 0.6, 1.0]
            ),
            expand=True,
            content=ft.Column(
                [
                    ft.Container(height=120),
                    ft.Icon(ft.Icons.FAVORITE_ROUNDED, size=120, color=ft.Colors.WHITE),
                    ft.Text("VURA", size = 45, font_family=fonts.FontsTitles.TITLE, color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER),
                    ft.Container(height=10),

                    ft.Container(expand=True),
                    ft.Text(
                        "Tu aplicación de salud\ntodo en uno",
                        size=13,
                        font_family = fonts.FontsApp.NORMAL,
                        color=ft.Colors.WHITE,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.ElevatedButton(
                        content = ft.Text(
                            "Iniciar Sesión", 
                            font_family = fonts.FontsApp.BOLD, 
                            color = "#14655B"),
                        on_click=lambda _: self.navigate_to("/login"),
                        width = 200,
                        height = 50,
                        style = ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=40),
                            bgcolor=ft.Colors.WHITE,
                            color = "#013F4A",
                        ),
                    ),
                    ft.Container(height=0),
                    ft.OutlinedButton(
                        content = ft.Text(
                            "Crear Cuenta",
                            font_family = fonts.FontsApp.BOLD,
                            color = ft.Colors.WHITE
                        ),
                        on_click=lambda _: self.navigate_to("/register"),
                        width=200,
                        height=50,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=40),
                            side=ft.BorderSide(2, ft.Colors.WHITE),
                            color = ft.Colors.WHITE,
                        ),
                    ),
                    ft.Container(height=60),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=50,
        )
