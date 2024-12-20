import flet as ft

from components.nav_bar import create_navbar


def main(page: ft.Page):
    # настройки страницы
    page.window_width = 370
    page.window_height = 750
    page.theme_mode = "dark"
    page.bgcolor = "#1E1E2F"
    page.padding = 0




    block = ft.Container(
        content=ft.Text("Привет, мир!", color="#FFFFFF"),
        bgcolor='#2A2A2F',
        width=500,
        height=100,
        padding=10,

        )

    navbar = create_navbar()

    page.add(block)

    page.add(navbar)



# Запускаем приложение
ft.app(target=main)

