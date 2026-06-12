import flet as ft
from views.welcome_view import WelcomeView
from views.login_view import LoginView
from views.register_view import RegisterView
from views.home_view import HomeView

def main(page: ft.Page):
    page.title = "Vura: The Health App"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Ajustes visuales para simular un móvil
    page.window_width = 390
    page.window_height = 800
    page.window_resizable = True

    def navigate_to(route):
        page.clean()  # Limpia la pantalla por completo
        
        if route == "/":
            page.add(WelcomeView(page, navigate_to))
        elif route == "/login":
            page.add(LoginView(page, navigate_to))
        elif route == "/register":
            page.add(RegisterView(page, navigate_to))
        elif route == "/home":
            page.add(HomeView(page, navigate_to))
        
        page.update()

    # Cargamos la pantalla inicial
    navigate_to("/")

if __name__ == "__main__":
    ft.app(target=main)
