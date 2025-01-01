import flet as ft

import requests
from auth.auth_logic

API_URL = "http://127.0.0.1:8000/api/"

# orders/new/
# customer/new/


class LogicCreateOrder:

    def __init__(self):
        self.SERVICE_TYPES = [
                ('1', 'Веб разработка'),
                ('2', 'Маркетинг'),
                ('3', 'Копирайтинг'),
                ('4', 'Рерайтиинг'),
                ('5', 'Переводы'),
                ('6', 'Видеомонтаж'),
                ('7', 'Фотография')
            ]

    def create_order(self, name, type, price: int, desc, executor : int):
        api = f"{API_URL}/orders/new/"
        data = {
            "name": name,
            "order_type": type,
            "price": price,
            "desc": desc,
            "executor ": executor
        }

        response = requests.post(api, json=data, headers=)
        if response.status_code == 201:
            return True
        else:
            return False

    def create_executor (self, user_id, phone):
        api = f"{API_URL}/customers/new/"
        data = {
            "user": user_id,
            "phone": phone,
        }

        response = requests.post(api, json=data)
        if response.status_code == 201:
            return True
        else:
            return False





class CreateOrderPage:

    def __init__(self):
        self.SERVICE_TYPES = [
                ('1', 'Веб разработка'),
                ('2', 'Маркетинг'),
                ('3', 'Копирайтинг'),
                ('4', 'Рерайтиинг'),
                ('5', 'Переводы'),
                ('6', 'Видеомонтаж'),
                ('7', 'Фотография')
            ]

    def build(self, switch_page):

        title_auth = ft.Text("Создать заказ", size=24, weight=ft.FontWeight.BOLD)

        name_oreder_input = ft.TextField(
            label="Имя заказа",
            bgcolor="#1E1E2F",
            color="#B2FF66",
            border_color="#B2FF66"
            )
        # Многострочное текстовое поле для описания заказа
        desc_order_input = ft.TextField(
            label="Описание заказа",
            bgcolor="#1E1E2F",
            color="#B2FF66",
            border_color="#B2FF66",
            multiline=True,  # Позволяет вводить многострочный текст
            # width=300,  # Ширина текстового поля
            height=200,  # Высота текстового поля
            max_length=500  # Максимальная длина текста
            )
        price_order_input = ft.TextField(
            label="Цена",
            bgcolor="#1E1E2F",
            color="#B2FF66", border_color="#B2FF66"
            )
        phone_order_input = ft.TextField(
            label="Номер телефона",
            bgcolor="#1E1E2F",
            color="#B2FF66", border_color="#B2FF66"
            )


        # Выпадающий список для выбора типа заказа
        type_order_input = ft.Dropdown(     # ft.dropdown.Option("Тип 1"),
            label="Тип заказа",
            options=[ft.dropdown.Option(name) for id, name in self.SERVICE_TYPES],
            bgcolor="#1E1E2F",
            color="#B2FF66",
            border_color="#B2FF66",
            # width=300
             )

        create_order_button = ft.ElevatedButton(
            text="Создать",
            bgcolor="#B2FF66",  # Цвет кнопки
            color="#1E1E2F",  # Цвет текста на кнопке
            )


        authorization_fields_column = ft.Column(
            controls=[
                name_oreder_input,
                type_order_input,
                price_order_input,
                phone_order_input,
                desc_order_input,
                create_order_button,
            ],
            # alignment=ft.MainAxisAlignment.CENTER,
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