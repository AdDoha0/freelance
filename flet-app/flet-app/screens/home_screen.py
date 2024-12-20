import flet as ft


class HomePage:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Главная страница"


    def build(self):
        # Заголовок "Популярные"
        popular_title = ft.Text("Популярные", size=24, weight=ft.FontWeight.BOLD)

        # Карточка с рекомендацией
        recommendation_card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Рекомендация: Проект А", size=18, weight=ft.FontWeight.NORMAL),
                    ft.Text("Описание: Это отличный проект для фрилансеров!", size=14),
                    ft.ElevatedButton("Подробнее", on_click=self.view_details)
                ]),
                padding=10
            ),
            elevation=2,
            width=300,
            height=150
        )

        # Категории
        categories_title = ft.Text("Категории", size=20, weight=ft.FontWeight.BOLD)
        categories = ft.Column([
            ft.TextButton("Веб-разработка"),
            ft.TextButton("Графический дизайн"),
            ft.TextButton("Копирайтинг"),
            ft.TextButton("Маркетинг"),
            ft.TextButton("Мобильные приложения"),
        ])

        # Возвращаем главный контейнер с элементами
        return ft.Column([
            popular_title,
            recommendation_card,
            categories_title,
            categories
        ])

    def view_details(self, e):
        # Здесь можно добавить логику для отображения деталей проекта
        print("Показать детали проекта")