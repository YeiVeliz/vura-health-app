import flet as ft
import time

# Animación de entrada suave para cualquier vista
def apply_fade_in_animation(view_content):
    view_content.opacity = 0
    view_content.animate_opacity = 800
    
    def trigger():
        time.sleep(0.1)
        view_content.opacity = 1
        view_content.update()
        
    return trigger

# Modificaremos el flujo de navegación para aplicar la animación
def navigate_with_animation(page, target_view_func, navigate_to):
    # 1. Creamos la vista
    new_view = target_view_func(page, navigate_to)
    
    # 2. Si es un Container, aplicamos la opacidad
    if isinstance(new_view, ft.Container):
        new_view.opacity = 0
        new_view.animate_opacity = 800
        
        # 3. Limpiamos y añadimos
        page.clean()
        page.add(new_view)
        page.update()
        
        # 4. Fade-in
        new_view.opacity = 1
        new_view.update()
    else:
        page.clean()
        page.add(new_view)
        page.update()
