import flet as ft


class LoginPage:

    def build(self, switch_page):

        title_login = ft.Text("Войдите  в акаунт", size=24,
                                weight=ft.FontWeight.BOLD)


        # Поля для ввода логина и пароля
        login_input = ft.TextField(
            label="Логин", bgcolor="#1E1E2F",
            color="#B2FF66", border_color="#B2FF66"
            )
        password_input = ft.TextField(
            label="Пароль", password=True,
            bgcolor="#1E1E2F", color="#B2FF66",
            border_color="#B2FF66"
            )


        # Кнопка для входа
        login_button = ft.ElevatedButton(
            text="Войти",
            bgcolor="#B2FF66",  # Цвет кнопки
            color="#1E1E2F",  # Цвет текста на кнопке
        )


        login_fields_column = ft.Column(
            controls=[
                login_input,
                password_input,
                login_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )





        layout = ft.Column(
            controls=[
                ft.Container(
                    content=title_login,
                    padding=ft.padding.only(bottom=10),
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=login_fields_column,
                    ),
            ],
            spacing=10,
            expand=True
        )



        return layout