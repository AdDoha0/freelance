import flet as ft
from flet import TemplateRoute

# from components.important_details import create_navbar

from screens.home_screen import HomePage
from screens.cat_or_search_screen import CatOrSearcPage
from screens.login_screen import LoginPage
from screens.authorization_screen import AuthorizationPage
from screens.profile_screen import ProfilePage
from screens.create_order_form_screen import CreateOrderPage
from screens.open_order_screens import OpenOrderPage


def main(page: ft.Page):
    # настройки страницы
    page.window.width = 370
    page.window.height = 750
    page.theme_mode = "dark"
    page.bgcolor = "#1E1E2F"
    page.padding = 12
    page.title = "Фриланс Приложение"

    page.appbar = ft.AppBar(
        title=ft.Text("Логотип", size=20, weight=ft.FontWeight.BOLD,
                      color="#B2FF66"),
        center_title=True,
        bgcolor="#1E1E2F",
    )

    def handle_route_change(route: str):
        page.clean()

        troute = TemplateRoute(route)

        if troute.match("/home"):
            home_page = HomePage(page)
            page.add(home_page.build())

        elif troute.match("/auth/login"):
            login_page = LoginPage(page)
            page.add(login_page.build())
        elif troute.match("/auth/authorization"):
            authorization_page = AuthorizationPage(page)
            page.add(authorization_page.build())

        elif troute.match("/search"):
            search_page = CatOrSearcPage(page)
            page.add(search_page.build())

        elif troute.match("/order/create_order"):
            create_order_page = CreateOrderPage(page)
            page.add(create_order_page.build())
        elif troute.match("/order"):
            open_order_page = OpenOrderPage(page)
            page.add(open_order_page.build())
        elif troute.match("/profile"):
            profile_page = ProfilePage(page)
            page.add(profile_page.build())
        else:
            page.add(ft.Text("404 - Page not found"))

        page.add(create_navbar(switch_page))

    def switch_page(route: str):
        page.route = route
        handle_route_change(route)




    def create_navbar(switch_page) -> ft.Row:
        navbar = ft.Row(
            controls=[
                ft.IconButton(
                    ft.icons.HOME,
                    tooltip="Главная",
                    icon_color="#B2FF66",
                    on_click=lambda e: switch_page("/home")
                ),
                ft.IconButton(
                    ft.icons.SEARCH_SHARP,
                    tooltip="Избранное",
                    icon_color="#B2FF66",
                    on_click=lambda e: switch_page("/search")
                ),
                ft.IconButton(
                    ft.icons.CONTACT_MAIL,
                    tooltip="Контакты",
                    icon_color="#B2FF66",
                    on_click=lambda e: switch_page("/profile")
                ),
                ft.IconButton(
                    ft.icons.WARNING,
                    tooltip="Тестовый лог",
                    icon_color="#B2FF66",
                    on_click=lambda e: switch_page("/auth/login")
                ),
                ft.IconButton(
                    ft.icons.WARNING,
                    tooltip="Тестовый лог",
                    icon_color="#B2FF66",
                    on_click=lambda e: switch_page("/auth/authorization")
                ),

            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
        return ft.Container(
            content=navbar,
            bgcolor="#1A1A2E",
            padding=ft.padding.only(top=20, bottom=15),
            margin=ft.margin.only(left=-12, right=-12, top=-12, bottom=-12)
        )

    switch_page("/home")

if __name__ == "__main__":
    ft.app(target=main)
