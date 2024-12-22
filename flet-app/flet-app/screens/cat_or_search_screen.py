import flet as ft
from components.important_details import OrderCard, create_search_form


class CatOrSearcPage:

    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Заказы"

    def build(self):

        search_form = create_search_form()

        result_title = ft.Text("Результат", size=17, weight=ft.FontWeight.BOLD)

        recomend_order_card_test1 = OrderCard(
            name="Разработать веб-сайт",
            type="Веб-разработка", price=500,
            description="Создание современного адаптивного сайта для бизнеса"
        ).card
        recomend_order_card_test2 = OrderCard(
            name="Разработать веб-сайт",
            type="Веб-разработка", price=500,
            description="Создание современного адаптивного сайта для бизнеса"
        ).card
        recomend_order_card_test3 = OrderCard(
            name="Разработать веб-сайт",
            type="Веб-разработка", price=500,
            description="Создание современного адаптивного сайта для бизнеса"
        ).card

        # Создание прокручиваемой области для карточек заказов
        order_cards_column = ft.Column(
            [
                recomend_order_card_test1,
                recomend_order_card_test2,
                recomend_order_card_test3,
            ],
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
                ft.Container(
                    content=search_form,
                    padding=ft.padding.only(bottom=0)
                ),
                ft.Container(
                    content=result_title,
                    padding=ft.padding.only(top=2),
                ),
                ft.Container(
                    content=order_cards_list_view,
                    # padding=ft.padding.only(top=0),
                    # clip_behavior=ft.ClipBehavior.HARD_EDGE
                ),
            ],
            spacing=10,
            expand=True
        )

        return layout
