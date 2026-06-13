import flet as ft
from views.welcome_view import WelcomeView
from views.login_view import LoginView
from views.register_view import RegisterView
from views.home_view import HomeView

def main(page: ft.Page):
    # Configuración de ventana tipo móvil
    page.window.width = 390
    page.window.height = 800
    page.window.resizable = False  
    page.window.maximizable = False
    
    page.title = "Vura: The Health App"
    page.theme_mode = ft.ThemeMode.LIGHT

    def navigate_to(route):
        # 1. Determinar qué vista mostrar
        if route == "/": view = WelcomeView(page, navigate_to)
        elif route == "/login": view = LoginView(page, navigate_to)
        elif route == "/register": view = RegisterView(page, navigate_to)
        elif route == "/home": view = HomeView(page, navigate_to)
        else: view = WelcomeView(page, navigate_to)
        
        # 2. Configurar la animación (Fade-in)
        # Aplicamos opacidad inicial al contenedor raíz de la vista
        view.opacity = 0
        view.animate_opacity = 500  # Animación de 500ms
        
        # 3. Limpiar y añadir
        page.clean()
        page.add(view)
        page.update()
        
        # 4. Trigger de la animación (usamos un pequeño delay para asegurar la transición)
        view.opacity = 1
        view.update()

    # Cargamos la pantalla inicial
    navigate_to("/")

if __name__ == "__main__":
    ft.app(target=main)
