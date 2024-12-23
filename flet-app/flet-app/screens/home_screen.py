import flet as ft
from components.important_details import create_navbar, create_cat_scroll_horizontal, OrderCard


class HomePage:

    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Главная страница"

    def build(self):

        # Заголовок "Популярные"
        popular_title = ft.Text("Рекомендации", size=24,
                                weight=ft.FontWeight.BOLD)

        recomend_order_card = OrderCard(name="Разработать веб-сайт",
                                        type="Веб-разработка", price=500, description="Создание современного адаптивного сайта для бизнеса").card

        # Категории
        categories_title = ft.Text(
            "Популярные", size=20, weight=ft.FontWeight.BOLD)

        categories = create_cat_scroll_horizontal()

        layout = ft.Column(
            controls=[
                ft.Container(
                    content=popular_title,
                    padding=ft.padding.only(bottom=10)
                ),
                ft.Container(
                    content=recomend_order_card,
                ),
                ft.Container(
                    content=categories_title,
                ),
                ft.Container(
                    content=categories,
                ),
            ],
            spacing=10,
            expand=True
        )

        # Возвращаем главный контейнер с элементами
        return layout
