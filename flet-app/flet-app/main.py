import flet as ft


from components.important_details import create_navbar

from screens.home_screen import HomePage
from screens.cat_or_search_screen import CatOrSearcPage
from screens.login_screen import LoginPage
from screens.authorization_screen import AuthorizationPage
from screens.profile_screen import ProfilePage
from screens.create_order_form_screen import CreateOrderPage







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
    )

    pages = {
            "home": HomePage(page),
            "cat_or_search": CatOrSearcPage(page),
            "login": LoginPage(page),
            "authorization": AuthorizationPage(page),
            "profile": ProfilePage(page),
            "create_order": CreateOrderPage(page)
        }

    def switch_page(page_name):
        page.clean()  # Очищаем текущую страницу
        page.add(pages[page_name].build())  # Добавляем новую страницу
        page.add(create_navbar(switch_page))


    page.on_route_change = switch_page


    # Добавляем первую страницу
    switch_page("home")


    # # Создаем экземпляры страниц
    # home_page = HomePage(page)
    # cat_or_search_page = CatOrSearcPage(page)
    # login_page = LoginPage(page)
    # authorization_page = AuthorizationPage(page)
    # profile_page = ProfilePage(page)
    # create_order_page = CreateOrderPage(page)



    # # Функция для переключения страниц
    # def switch_page(page_name):
    #     page.clean()  # Очищаем текущую страницу

    #     if page_name == "home":
    #         page.add(home_page.build())  # Добавляем главную страницу
    #     elif page_name == "cat_or_search":
    #         page.add(cat_or_search_page.build())  # Добавляем вторую страницу
    #     elif page_name == "login":
    #         page.add(login_page.build())
    #     elif page_name == "authorization":
    #         page.add(authorization_page.build())
    #     elif page_name == "profile":
    #         page.add(profile_page.build())
    #     elif page_name == "create_order":
    #         page.add(create_order_page.build())

    #     page.add(create_navbar(switch_page))


    # Добавляем страницы в приложение
    # switch_page("home")
    # page.add(create_navbar())


if __name__ == "__main__":
    ft.app(target=main)






