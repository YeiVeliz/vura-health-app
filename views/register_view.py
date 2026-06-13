import flet as ft
import time
from utils.firebase_config import auth

def RegisterView(page: ft.Page, navigate_to):
    input_style = dict(
        filled=True,
        fill_color=ft.Colors.GREY_100,
        border_color=ft.Colors.TRANSPARENT,
        border_radius=20,
        content_padding=ft.Padding(20, 15, 20, 15),
    )

    full_name = ft.TextField(label="Full Name", **input_style)
    email = ft.TextField(label="Email", **input_style)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True, **input_style)
    
    def handle_register(e):
        try:
            user = auth.create_user_with_email_and_password(email.value, password.value)
            page.data = {"user": user}
            navigate_to("/home")
        except:
            pass

    container = ft.Container(
        bgcolor=ft.Colors.BLUE_700,
        expand=True,
        content=ft.Column([
            ft.Container(height=40),
            ft.Row([ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: navigate_to("/"), icon_color=ft.Colors.WHITE)]),
            ft.Container(height=10),
            ft.Container(
                padding=ft.Padding(30, 0, 0, 0),
                content=ft.Text("Get Started", size=32, weight="bold", color=ft.Colors.WHITE),
            ),
            ft.Container(height=20),
            ft.Container(
                bgcolor=ft.Colors.WHITE,
                border_radius=ft.BorderRadius(40, 40, 0, 0),
                padding=40,
                expand=True,
                content=ft.Column([
                    full_name,
                    ft.Container(height=15),
                    email,
                    ft.Container(height=15),
                    password,
                    ft.Container(height=25),
                    ft.ElevatedButton(
                        "Sign up", 
                        width=float("inf"), 
                        height=55, 
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=20), 
                            bgcolor=ft.Colors.BLUE_700, 
                            color=ft.Colors.WHITE
                        )
                    ),
                    ft.Container(height=30),
                    ft.Divider(color=ft.Colors.GREY_300),
                    ft.Container(height=20),
                    ft.Text("Sign up with", color=ft.Colors.GREY_500, text_align=ft.TextAlign.CENTER),
                    ft.Container(height=15),
                    ft.Row([
                        ft.IconButton(ft.Icons.FACEBOOK, icon_color=ft.Colors.BLUE_800), 
                        ft.IconButton(ft.Icons.G_MOBILEDATA, icon_color=ft.Colors.RED_600), 
                        ft.IconButton(ft.Icons.APPLE, icon_color=ft.Colors.BLACK)
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Container(expand=True),
                    ft.Row([ft.Text("Already have an account?"), ft.TextButton("Sign in", on_click=lambda _: navigate_to("/login"))], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Container(height=20)
                ], spacing=0)
            )
        ], spacing=0)
    )

    async def animate_in():
        time.sleep(0.05)
        container.opacity = 1
        container.update()
    
    container.opacity = 0
    container.animate_opacity = 500
    page.run_task(animate_in)
    
    return container
