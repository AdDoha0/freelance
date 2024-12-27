import flet as ft



class CatScroll:

    ORDER_TYPES = [
                'Веб разработка','Маркетинг',
                'Копирайтинг','Рерайтиинг',
                'Переводы','Видеомонтаж','Фотография'
            ]

    def __init__(self, page: ft.Page):
        self.page = page


    def build(self):
        # Создselfаем список круглых кнопок
        categoselfry_buttons  = [
            ft.Container(
                content=ft.TextButton("it", style=ft.ButtonStyle(color=ft.colors.WHITE)),
                border_radius=50,  # Радиус границы для круглой формы
                border=ft.border.all(color="#B2FF66"),
                width=100,  # Ширина кнопки
                height=100,  # Высота кнопки
                on_click=self.open_category(1)
            ),
        ]

        def open_category(self, category_id):
            def handler(e):
                # Изменяем маршрут на выбранную категорию
                self.page.route = f"/category/{category_id}"  # Устанавливаем новый маршрут
                self.page.update()  # Обновляем страницу для отображения изменений

            return handler

