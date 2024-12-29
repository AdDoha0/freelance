import  flet as ft




def create_navbar(page: ft.Page) -> ft.Row:
    from route_handler import RouteHandler
    route = RouteHandler(page)
    navbar = ft.Row(
        controls=[
            ft.IconButton(
                ft.icons.HOME,
                tooltip="Главная",
                icon_color="#B2FF66",
                on_click=lambda e: route.switch_page("/home")
            ),
            ft.IconButton(
                ft.icons.SEARCH_SHARP,
                tooltip="Избранное",
                icon_color="#B2FF66",
                on_click=lambda e: route.switch_page("/orders/all")
            ),
            ft.IconButton(
                ft.icons.CONTACT_MAIL,
                tooltip="Контакты",
                icon_color="#B2FF66",
                on_click=lambda e: route.switch_page("/profile", )
            ),
            ft.IconButton(
                ft.icons.WARNING,
                tooltip="Тестовый лог",
                icon_color="#B2FF66",
                on_click=lambda e: route.switch_page("/auth/login")
            ),
            ft.IconButton(
                ft.icons.WARNING,
                tooltip="Тестовый лог",
                icon_color="#B2FF66",
                on_click=lambda e: route.switch_page("/auth/authorization")
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
