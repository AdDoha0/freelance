import flet as ft
import requests

from auth.auth_logic import Auth

API_URL = "http://127.0.0.1:8000/api"

class LoginPage:

    def __init__(self):
        self.auth = Auth()  # Создаем экземпляр Auth


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
            on_click=lambda e: self.handle_login(login_input.value, password_input.value, switch_page)
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

    def handle_login(self, login, password, switch_page):
            if self.auth.login(login, password):
                print("Успешный вход")
                switch_page("/home")  # Переключение на домашнюю страницу
            else:
                print("Ошибка входа")  # Обработка ошибки

