import flet as ft

class AppColors:
    # --- Paleta de Verdes ---
    GREEN_PRIMARY = "#2E7D32"
    GREEN_DARK = "#1B5E20"
    GREEN_LIGHT = "#81C784"
    
    # --- Paleta de Azules ---
    BLUE_DARK = "#0D47A1"
    BLUE_PRIMARY = "#1976D2"
    
    # --- Neutros ---
    WHITE = ft.Colors.WHITE
    GREY_100 = ft.Colors.GREY_100
    GREY_300 = ft.Colors.GREY_300
    GREY_500 = ft.Colors.GREY_500

class AppStyles:
    # Usamos la paleta de colores para definir los estilos
    PRIMARY_COLOR = AppColors.BLUE_DARK
    PRIMARY_DARK = AppColors.BLUE_DARK
    SECONDARY_COLOR = AppColors.GREEN_PRIMARY
    
    INPUT_STYLE = dict(
        filled=True,
        fill_color=AppColors.GREY_100,
        border_color=ft.Colors.TRANSPARENT,
        border_radius=20,
        content_padding=ft.Padding(20, 15, 20, 15),
    )

    @staticmethod
    def get_elevated_button_style(bgcolor=SECONDARY_COLOR):
        return ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=20),
            bgcolor=bgcolor,
            color=AppColors.WHITE,
        )