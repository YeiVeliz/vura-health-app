import flet as ft

class WelcomeView(ft.View):
    def __init__(self, page: ft.Page, navigate_to):
        super().__init__(route="/")
        self.page_ref = page
        self.navigate_to = navigate_to
        self.controls = [self._build_content()]

    def _build_content(self):
        return ft.Container(
            gradient= ft.LinearGradient(
                begin=ft.Alignment.TOP_CENTER,
                end=ft.Alignment.BOTTOM_CENTER,
                colors=[
                    "#013F4A", 
                    "#068562"
                    ],
                    stops = [0.0, 0.6]
            ),
            expand=True,
            content=ft.Column(
                [
                    ft.Container(height=120),
                    ft.Icon(ft.Icons.FAVORITE_ROUNDED, size=120, color=ft.Colors.WHITE),
                    ft.Text("VURA", size = 45, weight="bold", color=ft.Colors.WHITE),
                    ft.Container(height=10),

                    ft.Container(expand=True),
                    ft.Text(
                        "Tu aplicación de salud todo en uno",
                        size=14,
                        color=ft.Colors.WHITE,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.ElevatedButton(
                        "Iniciar Sesión",
                        on_click=lambda _: self.navigate_to("/login"),
                        width = 300,
                        height = 50,
                        style = ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=40),
                            bgcolor=ft.Colors.WHITE,
                            color = "#013F4A",
                        ),
                    ),
                    ft.Container(height=5),
                    ft.OutlinedButton(
                        "Crear Cuenta",
                        on_click=lambda _: self.navigate_to("/register"),
                        width=300,
                        height=50,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=40),
                            side=ft.BorderSide(2, ft.Colors.WHITE),
                            color = ft.Colors.WHITE,
                        ),
                    ),
                    ft.Container(height=50),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=30,
        )
