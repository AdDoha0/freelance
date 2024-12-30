import flet as ft
from flet import TemplateRoute

from screens.home_screen import HomePage
from screens.cat_or_search_screen import CatOrSearcPage
from auth.login_screen import LoginPage
from auth.authorization_screen import AuthorizationPage
from screens.profile_screen import ProfilePage
from screens.create_order_form_screen import CreateOrderPage
from screens.open_order_screens import OpenOrderPage
from components.navbar import create_navbar


class RouteHandler:
    def __init__(self, page: ft.Page):
        self.page = page

    def switch_page(self, route: str):
        self.handle_route_change(route)

    def handle_route_change(self, route: str):
        print(f"Route changed to: {route}")  # Логирование
        self.page.clean()

        troute = TemplateRoute(route)

        if troute.match("/home"):
            home_page = HomePage()
            self.page.add(home_page.build(self.switch_page))

        elif troute.match("/auth/login"):
            login_page = LoginPage()
            self.page.add(login_page.build(self.switch_page))

        elif troute.match("/auth/authorization"):
            authorization_page = AuthorizationPage()
            self.page.add(authorization_page.build(self.switch_page))

        elif troute.match("/orders/all"):
            cat_page = CatOrSearcPage()
            self.page.add(cat_page.build(self.switch_page))

        elif troute.match("/orders/:cat_id"):
            cat_id = troute.cat_id
            print(f"Category ID: {cat_id}")
            cat_page = CatOrSearcPage(cat_id)
            self.page.add(cat_page.build(self.switch_page))

        elif troute.match("/order/create_order"):
            create_order_page = CreateOrderPage()
            self.page.add(create_order_page.build(self.switch_page))

        elif troute.match("/order"):
            open_order_page = OpenOrderPage()
            self.page.add(open_order_page.build(self.switch_page))

        elif troute.match("/profile"):
            profile_page = ProfilePage()
            self.page.add(profile_page.build(self.switch_page))

        else:
            self.page.add(ft.Text("404 - Page not found"))

        self.page.add(create_navbar(self.page))
