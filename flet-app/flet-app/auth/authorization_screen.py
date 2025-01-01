import flet as ft

from auth.auth_logic import Auth

class AuthorizationPage:

    def __init__(self):
        self.auth = Auth()

    def build(self, switch_page):

        title_auth = ft.Text("Авторизация", size=24, weight=ft.FontWeight.BOLD)


        username_input = ft.TextField(
            label="Имя пользователя",
            bgcolor="#1E1E2F",
            color="#B2FF66",
            border_color="#B2FF66"
            )
        password_input = ft.TextField(
            label="Пароль", password=True,
            bgcolor="#1E1E2F", color="#B2FF66",
            border_color="#B2FF66"
            )
        # email_input = ft.TextField(
        #     label="Электронная почта",
        #     bgcolor="#1E1E2F",
        #     color="#B2FF66", border_color="#B2FF66"
        #     )

        login_button = ft.ElevatedButton(
            text="Войти",
            bgcolor="#B2FF66",  # Цвет кнопки
            color="#1E1E2F",  # Цвет текста на кнопке
            on_click=lambda e: self.handle_auth(username_input.value, password_input.value, switch_page)

            )


        authorization_fields_column = ft.Column(
            controls=[
                username_input,
                # email_input,
                password_input,
                login_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        layout = ft.Column(
            controls=[
                ft.Container(
                    content=title_auth,
                    padding=ft.padding.only(bottom=10),
                    alignment=ft.alignment.center
                    ),
                ft.Container(
                    content=authorization_fields_column,
                    ),
                ],
                spacing=10,
                expand=True
            )
        return layout

    def handle_auth(self, username, password, switch_page):
            if self.auth.registration(username, password):
                print("Успешная регистрация")
                switch_page("/auth/login")  # Переключение на домашнюю страницу
            else:
                print("Ошибка входа в функции handle_auth")  # Обработка ошибки
