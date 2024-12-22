import flet as ft

from components.important_details import create_navbar
from screens.home_screen import HomePage
from screens.cat_or_search_screen import CatOrSearcPage

def main(page: ft.Page):
    # настройки страницы
    page.window_width = 370
    page.window_height = 750
    page.theme_mode = "dark"
    page.bgcolor = "#1E1E2F"
    page.padding = 12
    page.title = "Фриланс Приложение"


    page.appbar = ft.AppBar(
        title=ft.Text("Логотип", size=20, weight=ft.FontWeight.BOLD, color="#B2FF66"),  # Логотип в виде текста
        center_title=True,  # Центрирование заголовка
        bgcolor="#1E1E2F",  # Цвет фона AppBar
        # elevation=4,  # Тень под AppBar
    )



    # Создаем экземпляры страниц
    home_page = HomePage(page)
    cat_or_page = CatOrSearcPage(page)

    # Добавляем страницы в приложение


    page.add(home_page.build())
    page.add(create_navbar())


if __name__ == "__main__":
    ft.app(target=main)






