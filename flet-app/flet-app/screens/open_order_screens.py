import flet as ft


class OpenOrderPage:

    def __init__(self, page: ft.Page):
        self.page = page


    def build(self):
        title = ft.Text("Профиль", size=24, weight=ft.FontWeight.BOLD)




        layout = ft.Column(
            controls=[
                ft.Container(
                    content=title,
                    padding=ft.padding.only(bottom=10)
                ),
                ],
            spacing=10,
            expand=True
        )

        return layout

