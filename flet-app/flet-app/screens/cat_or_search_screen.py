import flet as ft
from components.important_details import OrderCard, create_search_form
import requests

class CatOrSearcPage:

    def __init__(self, cat_id=None):
        self.cat_id = cat_id # если передали категорию тут будет ее id, если нет тут будет None


    def fetch_orders(self):

        if self.cat_id is None:
            api_url = "http://127.0.0.1:8000/api/orders/all/" # URL вашего API для получения заказов по категориям
        else:
            api_url = f"http://127.0.0.1:8000/api/orders/all/?order_type={self.cat_id}"   # URL вашего API для получения всех заказов


        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                return response.json()  # Возвращает список заказов в формате JSON
            else:
                print(f"Ошибка при получении данных: {response.status_code}")
                return []  # Возвращает пустой список в случае ошибки
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return []  # Возвращает пустой список в случае исключения


    def build(self, switch_page):
        search_form = create_search_form()
        result_title = ft.Text("Результат", size=17, weight=ft.FontWeight.BOLD)


        # Получаем заказы из API
        orders = self.fetch_orders()

        # Создание карточек заказов на основе полученных данных
        order_cards = []
        for order in orders:
            order_card = OrderCard(
                name=order['name'],
                type=order['order_type'],
                price=order['price'],
                description=order['desc']
            ).card
            order_cards.append(order_card)




        # Создание прокручиваемой области для карточек заказов
        order_cards_column = ft.Column(
            controls=order_cards,
            spacing=10,
        )

        # Используем ListView для прокрутки
        order_cards_list_view = ft.ListView(
            controls=[order_cards_column],
            height=385, # Установите высоту для области прокрутки
            # auto_scroll=True, # Включение прокрутки, если содержимое превышает высоту
        )


        # Основной контейнер для всей структуры
        layout = ft.Column(
            [
                ft.Container(content=search_form, padding=ft.padding.only(bottom=0)),
                ft.Container(content=result_title, padding=ft.padding.only(top=2)),
                ft.Container(content=order_cards_list_view),
            ],
            spacing=10,
            expand=True
        )

        return layout
