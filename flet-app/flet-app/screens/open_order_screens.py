import flet as ft


class OpenOrderPage:



    def build(self, switch_page):
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

