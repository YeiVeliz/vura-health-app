import flet as ft
from utils.firebase_config import auth

class LoginView(ft.View):
    def __init__(self, page: ft.Page, navigate_to):
        super().__init__(route="/login")
        self.page_ref = page
        self.navigate_to = navigate_to
        self.input_style = dict(
            filled=True,
            fill_color=ft.Colors.GREY_100,
            border_color=ft.Colors.TRANSPARENT,
            border_radius=20,
            content_padding=ft.Padding(20, 15, 20, 15),
        )
        self.controls = [self._build_content()]

    def _build_content(self):
        email = ft.TextField(label="Email", **self.input_style)
        password = ft.TextField(label="Password", password=True, can_reveal_password=True, **self.input_style)
        
        container = ft.Container(
            bgcolor=ft.Colors.BLUE_700,
            expand=True,
            content=ft.Column([
                ft.Container(height=40),
                ft.Row([ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: self.navigate_to("/"), icon_color=ft.Colors.WHITE)]),
                ft.Container(height=20),
                ft.Container(
                    bgcolor=ft.Colors.WHITE,
                    border_radius=ft.BorderRadius(40, 40, 0, 0),
                    padding=40,
                    expand=True,
                    content=ft.Column([
                        ft.Text("Welcome back", size=28, weight="bold", color=ft.Colors.BLUE_900),
                        ft.Container(height=30),
                        email,
                        ft.Container(height=15),
                        password,
                        ft.Container(height=5),
                        ft.Row([ft.TextButton("Forgot password?", on_click=lambda _: None)], alignment=ft.MainAxisAlignment.END),
                        ft.Container(height=35),
                        ft.ElevatedButton(
                            "Sign In", 
                            on_click=lambda e: self.handle_login(email.value, password.value),
                            width=float("inf"), 
                            height=55, 
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=20), 
                                bgcolor=ft.Colors.BLUE_700, 
                                color=ft.Colors.WHITE
                            )
                        ),
                        ft.Container(height=45),
                        ft.Divider(color=ft.Colors.GREY_300),
                        ft.Container(height=20),
                        ft.Text("Sign in with", color=ft.Colors.GREY_500, text_align=ft.TextAlign.CENTER),
                        ft.Container(height=15),
                        ft.Row([
                            ft.IconButton(ft.Icons.FACEBOOK, icon_color=ft.Colors.BLUE_800), 
                            ft.IconButton(ft.Icons.G_MOBILEDATA, icon_color=ft.Colors.RED_600), 
                            ft.IconButton(ft.Icons.APPLE, icon_color=ft.Colors.BLACK)
                        ], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Container(expand=True),
                        ft.Row([ft.Text("Don't have an account?"), ft.TextButton("Sign up", on_click=lambda _: self.navigate_to("/register"))], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Container(height=20)
                    ], spacing=0)
                )
            ], spacing=0)
        )
        return container

    def handle_login(self, email, password):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            self.page_ref.data = {"user": user}
            self.navigate_to("/home")
        except Exception as e:
            print(f"Error login: {e}")
