# main.py
import flet as ft

def main(page: ft.Page):
    # Configuración inicial de la página principal
    page.title = "Navegación de Colores"
    page.bgcolor = ft.colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Función para cambiar a la página amarilla
    def ir_a_pagina_amarilla(e):
        page.views.append(
            ft.View(
                "/amarillo",
                bgcolor=ft.colors.YELLOW,
                controls=[
                    ft.Container(
                        content=ft.ElevatedButton(
                            text="Volver",
                            on_click=lambda _: regresar(),
                            style=ft.ButtonStyle(
                                bgcolor=ft.colors.BLACK,
                                color=ft.colors.WHITE,
                                padding=20,  # Tamaño interno del botón
                                text_style=ft.TextStyle(size=18),  # Tamaño del texto
                            )
                        ),
                        alignment=ft.alignment.center,  # Centra el botón
                        padding=20,  # Espaciado externo alrededor del botón
                    )
                ]
            )
        )
        page.update()

    # Función para cambiar a la página azul
    def ir_a_pagina_azul(e):
        page.views.append(
            ft.View(
                "/azul",
                bgcolor=ft.colors.BLUE,
                controls=[
                    ft.Container(
                        content=ft.ElevatedButton(
                            text="Volver",
                            on_click=lambda _: regresar(),
                            style=ft.ButtonStyle(
                                bgcolor=ft.colors.WHITE,
                                color=ft.colors.BLACK,
                                padding=20,  # Tamaño interno del botón
                                text_style=ft.TextStyle(size=18),  # Tamaño del texto
                            )
                        ),
                        alignment=ft.alignment.center,  # Centra el botón
                        padding=20,  # Espaciado externo alrededor del botón
                    )
                ]
            )
        )
        page.update()

    # Función para regresar a la página principal
    def regresar():
        if len(page.views) > 1:
            page.views.pop()
            page.update()

    # Crear botones circulares
    boton_amarillo = ft.ElevatedButton(
        text="Amarillo",
        on_click=ir_a_pagina_amarilla,  # Acción al pulsar
        style=ft.ButtonStyle(
            shape=ft.CircleBorder(),
            bgcolor=ft.colors.YELLOW,
            color=ft.colors.BLACK,
        ),
        width=70,
        height=70
    )

    boton_azul = ft.ElevatedButton(
        text="Azul",
        on_click=ir_a_pagina_azul,  # Acción al pulsar
        style=ft.ButtonStyle(
            shape=ft.CircleBorder(),
            bgcolor=ft.colors.BLUE,
            color=ft.colors.WHITE,
        ),
        width=70,
        height=70
    )

    # Agregar botones a la página principal
    page.add(
        ft.Row(
            controls=[boton_amarillo, boton_azul],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

# Ejecutar la app
if __name__ == "__main__":
    ft.app(target=main)
