import flet as ft

from route_handler import RouteHandler

def main(page: ft.Page):
    route_handler = RouteHandler(page)  # Создаем экземпляр RouteHandler

    # настройки страницы
    page.window.width = 370
    page.window.height = 750
    page.theme_mode = "dark"
    page.bgcolor = "#1E1E2F"
    page.padding = 12
    page.title = "Freealce"
    page.appbar = ft.AppBar(
        title=ft.Text("Логотип", size=20, weight=ft.FontWeight.BOLD,
                      color="#B2FF66"),
        center_title=True,
        bgcolor="#1E1E2F",
    )

    route_handler.switch_page("/home")


if __name__ == "__main__":
    ft.app(target=main)
