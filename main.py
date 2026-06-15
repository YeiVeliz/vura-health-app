import flet as ft
import os
from utils.navigation import Router

def main(page: ft.Page):
    # --- BLOQUE DE CARGA DE FUENTES ---
    page.fonts = {}
    fonts_dir = os.path.join(os.path.dirname(__file__), "assets", "fonts")
    
    if os.path.exists(fonts_dir):
        for filename in os.listdir(fonts_dir):
            if filename.lower().endswith((".ttf", ".otf")):
                font_name = os.path.splitext(filename)[0]
                # Flet necesita la ruta relativa a 'assets', por eso usamos 'fonts/...'
                page.fonts[font_name] = f"fonts/{filename}"
        print("Fuentes cargadas:", page.fonts)
    else:
        print("Carpeta de fuentes no encontrada en:", fonts_dir)
    # -----------------------------------

    page.window.width = 390
    page.window.height = 800
    page.window.resizable = False  
    page.window.maximizable = False
    
    page.title = "Vura: The Health App"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Inicializamos el gestor de rutas
    router = Router(page)
    
    # Cargamos la pantalla inicial (el Splash)
    router.navigate_to("/splash")

if __name__ == "__main__":
    ft.app(target=main)
