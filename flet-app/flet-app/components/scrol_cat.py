import flet as ft



class CatScroll:
    ORDER_TYPES = [
                ('1', 'Веб разработка'),
                ('2', 'Маркетинг'),
                ('3', 'Копирайтинг'),
                ('4', 'Рерайтиинг'),
                ('5', 'Переводы'),
                ('6', 'Видеомонтаж'),
                ('7', 'Фотография')
            ]



    def build(self, switch_page):

        category_buttons = [
            self.create_category_button(category, switch_page) for category in self.ORDER_TYPES
        ]

        # Создаем контейнер с горизонтальной прокруткой для кнопок категорий
        categories = ft.Container(
            content=ft.Row(controls=category_buttons, scroll=ft.ScrollMode.HIDDEN),  # Размещаем кнопки в строке
            width=370,  # Ширина контейнера
            height=100,  # Высота контейнера, чтобы кнопки помещались удобно
            alignment=ft.alignment.center  # Центрируем содержимое контейнера
        )

        return categories  # Возвращаем созданный контейнер с кнопками


    def create_category_button(self, category, switch_page):
        """Создает кнопку для заданной категории."""
        # Создаем контейнер для кнопки с заданными параметрами
        button = ft.Container(
            content=ft.TextButton(
                category[1],  # Отображаем название категории
                style=ft.ButtonStyle(color=ft.colors.WHITE),  # Задаем стиль кнопки
                on_click=lambda e: self.open_category(category[0], switch_page)  # Передаем ID категории при нажатии
            ),
            border_radius=50,  # Радиус границы для круглой формы
            border=ft.border.all(color="#B2FF66"),  # Цвет границы кнопки
            width=100,  # Ширина кнопки
            height=100,  # Высота кнопки
        )
        return button  # Возвращаем созданную кнопку



    def open_category(self, category: str, switch_page):
        """Определяет маршрут для каждой категории."""
        print(f"Opening category: {category}")  # Логирование
        category_route = f"/orders/{category}"
        switch_page(category_route)





