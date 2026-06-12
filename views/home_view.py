import flet as ft
from utils.firebase_config import db

def HomeView(page: ft.Page, navigate_to):
    # Obtener el correo del usuario logueado o usar uno por defecto para pruebas
    user_email = "Usuario de Vura"
    user_id = None
    if page.data and "user" in page.data:
        user_email = page.data["user"].get("email", user_email)
        user_id = page.data["user"].get("localId")

    # Estados iniciales (Métricas de Salud)
    water_count = [0]  # Usamos una lista para poder modificar el valor por referencia
    steps_count = [0]
    sleep_hours = [0.0]

    # Intentar cargar datos previos del usuario desde Firebase Realtime Database
    if user_id:
        try:
            stored_data = db.child("users").child(user_id).child("metrics").get().val()
            if stored_data:
                water_count[0] = stored_data.get("water", 0)
                steps_count[0] = stored_data.get("steps", 0)
                sleep_hours[0] = stored_data.get("sleep", 0.0)
        except Exception as e:
            print("No se pudieron descargar los datos de Firebase:", e)

    # Función para guardar datos en Firebase
    def save_metrics():
        if user_id:
            try:
                # Usamos child con una ruta directa y set al nodo padre si es necesario
                # O intentamos un método distinto:
                db.child("users").child(user_id).set({
                    "metrics": {
                        "water": water_count[0],
                        "steps": steps_count[0],
                        "sleep": sleep_hours[0]
                    }
                })
                print("Métricas guardadas exitosamente.")
            except Exception as e:
                print("Error al guardar en la nube (detallado):", e)


    # Textos que muestran los valores actuales en la interfaz
    water_text = ft.Text(f"{water_count[0]} vasos", size=22, weight="bold", color=ft.Colors.BLUE_900)
    steps_text = ft.Text(f"{steps_count[0]} pasos", size=22, weight="bold", color=ft.Colors.GREEN_900)
    sleep_text = ft.Text(f"{sleep_hours[0]} hrs", size=22, weight="bold", color=ft.Colors.PURPLE_900)

    # Lógica de Interacción
    def add_water(e):
        water_count[0] += 1
        water_text.value = f"{water_count[0]} vasos"
        save_metrics()
        page.update()

    def remove_water(e):
        if water_count[0] > 0:
            water_count[0] -= 1
            water_text.value = f"{water_count[0]} vasos"
            save_metrics()
            page.update()

    def add_steps(e):
        steps_count[0] += 1000
        steps_text.value = f"{steps_count[0]} pasos"
        save_metrics()
        page.update()

    def clear_steps(e):
        steps_count[0] = 0
        steps_text.value = f"{steps_count[0]} pasos"
        save_metrics()
        page.update()

    def add_sleep(e):
        sleep_hours[0] = round(sleep_hours[0] + 0.5, 1)
        sleep_text.value = f"{sleep_hours[0]} hrs"
        save_metrics()
        page.update()

    def remove_sleep(e):
        if sleep_hours[0] > 0:
            sleep_hours[0] = round(sleep_hours[0] - 0.5, 1)
            sleep_text.value = f"{sleep_hours[0]} hrs"
            save_metrics()
            page.update()

    # Botón de Cerrar Sesión
    def handle_logout(e):
        page.data = None
        navigate_to("/")

    # Tarjetas del Dashboard estilizadas
    water_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.WATER_DROP_ROUNDED, color=ft.Colors.BLUE_500, size=35),
                        title=ft.Text("Consumo de Agua", weight="bold"),
                        subtitle=ft.Text("Meta diaria: 8 vasos"),
                    ),
                    ft.Row(
                        [
                            water_text,
                            ft.Row(
                                [
                                    ft.IconButton(ft.Icons.REMOVE_CIRCLE_OUTLINE, on_click=remove_water, icon_color=ft.Colors.BLUE_600),
                                    ft.IconButton(ft.Icons.ADD_CIRCLE, on_click=add_water, icon_color=ft.Colors.BLUE_600),
                                ],
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    )
                ]
            ),
            padding=10,
        ),
        bgcolor=ft.Colors.BLUE_50
    )

    steps_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.DIRECTIONS_WALK_ROUNDED, color=ft.Colors.GREEN_500, size=35),
                        title=ft.Text("Pasos Diarios", weight="bold"),
                        subtitle=ft.Text("Meta diaria: 10,000 pasos"),
                    ),
                    ft.Row(
                        [
                            steps_text,
                            ft.Row(
                                [
                                    ft.IconButton(ft.Icons.REFRESH_ROUNDED, on_click=clear_steps, icon_color=ft.Colors.GREEN_600),
                                    ft.IconButton(ft.Icons.ADD_CIRCLE, on_click=add_steps, icon_color=ft.Colors.GREEN_600),
                                ],
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    )
                ]
            ),
            padding=10,
        ),
        bgcolor=ft.Colors.GREEN_50
    )

    sleep_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.BEDTIME_ROUNDED, color=ft.Colors.PURPLE_500, size=35),
                        title=ft.Text("Horas de Sueño", weight="bold"),
                        subtitle=ft.Text("Meta diaria: 8 horas"),
                    ),
                    ft.Row(
                        [
                            sleep_text,
                            ft.Row(
                                [
                                    ft.IconButton(ft.Icons.REMOVE_CIRCLE_OUTLINE, on_click=remove_sleep, icon_color=ft.Colors.PURPLE_600),
                                    ft.IconButton(ft.Icons.ADD_CIRCLE, on_click=add_sleep, icon_color=ft.Colors.PURPLE_600),
                                ],
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    )
                ]
            ),
            padding=10,
        ),
        bgcolor=ft.Colors.PURPLE_50
    )

    return ft.Container(
        content=ft.Column(
            [
                # Encabezado con datos del usuario
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("¡Hola!", size=16, color=ft.Colors.BLUE_GREY_600),
                                ft.Text(user_email.split("@")[0].capitalize(), size=24, weight="bold", color=ft.Colors.BLUE_900),
                            ],
                            spacing=2,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.LOGOUT_ROUNDED,
                            icon_color=ft.Colors.RED_600,
                            on_click=handle_logout,
                            tooltip="Cerrar Sesión",
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Divider(height=20),
                ft.Text("Tu Dashboard de Salud", size=20, weight="bold", color=ft.Colors.BLUE_GREY_900),
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                
                # Vista en scroll para las métricas
                ft.Column(
                    [
                        water_card,
                        steps_card,
                        sleep_card,
                    ],
                    scroll=ft.ScrollMode.AUTO,
                    expand=True,
                )
            ],
            expand=True,
        ),
        padding=20,
        expand=True,
    )
