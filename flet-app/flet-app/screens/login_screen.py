import flet as ft


class LoginPage:


    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Логин"


    def build(self):


        title_login = ft.Text("Войдите  в акаунт")




        layout = ft.Column(
            controls=[
                ft.Container(
                    content=title_login,
                    padding=ft.padding.only(bottom=10),
                    alignment=ft.alignment.center
                ),
            ],
            spacing=10,
            expand=True
        )



        return layout