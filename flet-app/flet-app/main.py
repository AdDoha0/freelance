import flet as ft

from components.navbar import create_navbar
from screens.home_screen import HomePage

def main(page: ft.Page):
    # настройки страницы
    page.window_width = 370
    page.window_height = 750
    page.theme_mode = "dark"
    page.bgcolor = "#1E1E2F"
    page.padding = 0
    page.title = "Фриланс Приложение"


    # Создаем экземпляры страниц
    home_page = HomePage(page)

    # Добавляем страницы в приложение
    page.add(home_page.build())


if __name__ == "__main__":
    ft.app(target=main)






