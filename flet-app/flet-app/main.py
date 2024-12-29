import flet as ft



from route_handler import RouteHandler

# from components.important_details import create_navbar

# from screens.home_screen import HomePage
# from screens.cat_or_search_screen import CatOrSearcPage
# from screens.login_screen import LoginPage
# from screens.authorization_screen import AuthorizationPage
# from screens.profile_screen import ProfilePage
# from screens.create_order_form_screen import CreateOrderPage
# from screens.open_order_screens import OpenOrderPage






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
