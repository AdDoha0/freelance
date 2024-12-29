import flet as ft


from components.important_details import  OrderCard
from components.scrol_cat import CatScroll


class HomePage:
    def build(self, switch_page):

        # Заголовок "Популярные"
        popular_title = ft.Text("Рекомендации", size=24,
                                weight=ft.FontWeight.BOLD)

        recomend_order_card = OrderCard(name="Разработать веб-сайт",
                                        type="Веб-разработка", price=500, description="Создание современного адаптивного сайта для бизнеса").card

        # Категории
        categories_title = ft.Text(
            "Популярные", size=20, weight=ft.FontWeight.BOLD)

        categories = CatScroll().build(switch_page)

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
