import flet as ft





def create_navbar(switch_page) -> ft.Row:
    # Создание навигационного бара внизу экрана
    navbar = ft.Row(
        controls=[
            ft.IconButton(ft.icons.HOME, tooltip="Главная", icon_color="#B2FF66", on_click=lambda e: switch_page("home")),
            ft.IconButton(ft.icons.SEARCH_SHARP, tooltip="Избранное", icon_color="#B2FF66", on_click=lambda e: switch_page("cat_or_search")),
            # ft.IconButton(ft.icons.INFO, tooltip="О нас", icon_color="#B2FF66"),
            ft.IconButton(ft.icons.CONTACT_MAIL, tooltip="Контакты", icon_color="#B2FF66", on_click=lambda e: switch_page("profile") ),
            ft.IconButton(ft.icons.WARNING, tooltip="test log", icon_color="#B2FF66", on_click=lambda e: switch_page("login")),
            ft.IconButton(ft.icons.WARNING, tooltip="test log", icon_color="#B2FF66", on_click=lambda e: switch_page("authorization")),

        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )

    # Обернем Row в Container для изменения стиля
    return ft.Container(
        content=navbar,
        bgcolor="#1A1A2E",
        padding=ft.padding.only(top=20, bottom=15),  # Установка отступов только сверху и снизу
        margin=ft.margin.only(left=-12, right=-12, top=-12, bottom=-12) # Установка отступов для контейнера
    )



def create_cat_scroll_horizontal() -> ft.Row:
        # Создаем список круглых кнопок
        buttons = [
            ft.Container(
                content=ft.TextButton("it", style=ft.ButtonStyle(color=ft.colors.WHITE)),
                border_radius=50,  # Радиус границы для круглой формы
                border=ft.border.all(color="#B2FF66"),
                width=100,  # Ширина кнопки
                height=100,  # Высота кнопки
            ),
            ft.Container(
                content=ft.TextButton("Веб", style=ft.ButtonStyle(color=ft.colors.WHITE) ),
                border_radius=50,
                border=ft.border.all(color="#B2FF66"),
                width=100,
                height=100,
            ),
            ft.Container(
                content=ft.TextButton("Дизайн", style=ft.ButtonStyle(color=ft.colors.WHITE)),
                border_radius=50,
                border=ft.border.all(color="#B2FF66",),
                width=100,
                height=100,
            ),
            ft.Container(
                content=ft.TextButton("Маркетинг", style=ft.ButtonStyle(color=ft.colors.WHITE) ),
                border_radius=50,
                border=ft.border.all(color="#B2FF66"),
                width=100,
                height=100,
            ),
        ]

        # Создаем контейнер с горизонтальной прокруткой
        categories = ft.Container(
            content=ft.Row(controls=buttons, scroll=ft.ScrollMode.HIDDEN),
            width=370,
            height=30,
            alignment=ft.alignment.center
        )

        return categories



class OrderCard():
    """Создание карточек заказов"""

    def __init__(self, name, type, price, description):
        self.order_name = name
        self.order_type = type
        self.order_price = price
        self.order_description = description
        self.card = self.create_order_card()


    def create_order_card(self):
        freelance_order_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Заказ", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                    ft.Divider(color="#B2FF66"),  # Разделитель
                    ft.Text(f"{self.order_name}", size=18, weight=ft.FontWeight.NORMAL, color=ft.colors.WHITE),
                    ft.Text(f"Тип: {self.order_type}", size=16, weight=ft.FontWeight.NORMAL, color=ft.colors.WHITE),
                    ft.Text(f"Цена: ${self.order_price}", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.YELLOW_400),
                    ft.Text(f"Описание: {self.order_description}",
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
        return freelance_order_card




class OrderCardInProfile:
    def __init__(self, order_name, order_type, order_price):
        self.order_name = order_name
        self.order_type = order_type
        self.order_price = order_price

    def create_order_card(self):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(self.order_name, size=16, weight=ft.FontWeight.BOLD),
                        ft.Text(f"Тип: {self.order_type}", size=14),
                        ft.Text(f"Цена: ${self.order_price}", size=14),
                        # ft.ElevatedButton("Подробнее",)
                    ],
                    spacing=5,
                    alignment=ft.MainAxisAlignment.START,


                ),
                padding=10,
                bgcolor='#1A1A2E',
            ),
            elevation=2,
            width=300,  # Установите нужную ширину
            height=120  # Установите нужную высоту
        )



def create_search_form():
    search_form = ft.Container(
        content=ft.Column(
            [
                ft.Text("Поиск заказов", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                ft.Row(
                    [
                        ft.TextField(
                            label="Введите название заказа",
                            # bgcolor='#1A1A2E',  # Цвет фона текстового поля
                            color=ft.colors.WHITE,
                            border_color="#B2FF66",  # Цвет границы текстового поля
                            cursor_color=ft.colors.WHITE,
                            expand=True  # Позволяет текстовому полю занимать доступное пространство
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,  # Выравнивание по левому краю
                    spacing=10  # Расстояние между элементами
                ),
                ft.Row(
                    [
                        ft.ElevatedButton(
                            "Найти",
                            color="#1E1E2F",
                            bgcolor="#B2FF66",
                            style=ft.ButtonStyle(padding=ft.padding.only(left=10, right=10))  # Паддинг для кнопки
                        )
                    ],
                    alignment=ft.MainAxisAlignment.START,  # Выравнивание по левому краю
                    spacing=10  # Расстояние между элементами
                )
            ],
            spacing=10,  # Расстояние между элементами
        ),
        bgcolor='#1E1E2F',  # Цвет фона контейнера формы поиска
    )
    return search_form




#vkvfkmmv
# bgcolor=ft.colors.TRANSPARENT, color=ft.colors.LIGHT_GREEN