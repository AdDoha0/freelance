import flet as ft
from components.important_details import create_navbar, create_cat_scroll_horizontal

class HomePage:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Главная страница"


    def build(self):

        # лого
        logo = ft.Image(ft.icons.LOGO_DEV, width=150, height=150)


        # Заголовок "Популярные"
        popular_title = ft.Text("Рекомендации", size=24, weight=ft.FontWeight.BOLD)

        # Карточка с рекомендацией
        # recommendation_card = ft.Card(
        #     content=ft.Container(
        #         content=ft.Column([
        #             ft.Text("Проект А", size=18, weight=ft.FontWeight.NORMAL),
        #             ft.Text("Описание: Это отличный проект для фрилансеров!", size=14),
        #             ft.ElevatedButton("Подробнее", color="#B2FF66")
        #         ]),
        #         padding=5,
        #     ),
        #     elevation=2,
        #     width=370,
        #     height=230,
        #     color='#1A1A2E'
        # )


        freelance_order_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Фриланс Заказ", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                    ft.Divider(color="#B2FF66"),  # Разделитель
                    ft.Text("Имя заказа: Разработка веб-сайта", size=18, weight=ft.FontWeight.NORMAL, color=ft.colors.WHITE),
                    ft.Text("Тип: Веб-разработка", size=16, weight=ft.FontWeight.NORMAL, color=ft.colors.WHITE),
                    ft.Text("Цена: \$500", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.YELLOW_400),
                    ft.Text("Описание: Создание современного и адаптивного веб-сайта для бизнеса.",
                            size=14, weight=ft.FontWeight.NORMAL, color=ft.colors.WHITE),
                    ft.Divider(color="#B2FF66"),  # Разделитель
                    ft.ElevatedButton(
                        "Подробнее",
                        color=ft.colors.WHITE,
                        style=ft.ButtonStyle(padding=ft.padding.only(top=10, bottom=10))  # Паддинг для кнопки
                    )
                ],
                spacing=10,  # Расстояние между элементами
                horizontal_alignment=ft.MainAxisAlignment.START  # Выравнивание по левому краю
            ),
            padding=20,
            bgcolor='#1A1A2E',  # Цвет фона карточки
        ),
        elevation=4,  # Эффект тени
        )




        # Категории
        categories_title = ft.Text("Популярные", size=20, weight=ft.FontWeight.BOLD)


        categories = create_cat_scroll_horizontal()
        navbar = create_navbar()



        main_content = ft.Column(
            controls=[
                ft.Container(
                    content=popular_title,
                    padding=ft.padding.only(bottom=10)
                    ),
                ft.Container(
                    content=freelance_order_card,
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

        layout = ft.Column(
            controls=[
                main_content,
                # Навигационная панель внизу
                ft.Container(content=navbar),
            ],
            expand=True  # Занимает доступное пространство
        )



        # Возвращаем главный контейнер с элементами
        return layout

    def view_details(self, e):
        # Здесь можно добавить логику для отображения деталей проекта
        print("Показать детали проекта")