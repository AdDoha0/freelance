import flet as ft



from components.important_details import OrderCardInProfile



# Пример данных пользователя
user_data = {
        "username": "Иван Иванов",
        "email": "ivan@example.com",
        "projects": [
            {"id": 1, "title": "Создание логотипа", "status": "В ожидании"},
            {"id": 2, "title": "Разработка сайта", "status": "В процессе"},
            {"id": 3, "title": "SEO-оптимизация", "status": "Завершен"},
        ],
    }



class ProfilePage:


    def build(self, switch_page):

        title_prof = ft.Text("Профиль", size=24, weight=ft.FontWeight.BOLD)



        general_information = ft.Column(
            controls=[
                ft.Text(f"{user_data['username']}", size=24, weight=ft.FontWeight.BOLD,),
                ft.Text(f"{user_data['email']}", size=16),
                ft.Divider(height=20, color="#B2FF66"),
                ft.Text("Ваши выставленные заказы:", size=20, weight=ft.FontWeight.BOLD),
            ],
             alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        )

        create_order_button = ft.ElevatedButton("добавить", bgcolor='#B2FF66', color=ft.colors.BLACK,
                            on_click=lambda e: self.page.on_route_change("create_order"))




        order_list = ft.Column(controls=[
            OrderCardInProfile("Дизайн логотипа", "Графический дизайн", 150).create_order_card(),
            OrderCardInProfile("Дизайн логотипа", "Графический дизайн", 150).create_order_card(),
            OrderCardInProfile("Дизайн логотипа", "Графический дизайн", 150).create_order_card(),
                ],
            scroll=ft.ScrollMode.ADAPTIVE,

            )


        layout = ft.Column(
            controls=[
                ft.Container(
                    content=title_prof,
                    padding=ft.padding.only(bottom=10)
                ),
                ft.Container(
                    content=general_information,
                    # padding=ft.padding.only(bottom=10)
                ),
                ft.Container(
                    content=create_order_button,
                    # padding=ft.padding.only(bottom=10)
                ),
                ft.Container(
                    content=order_list,
                    height=320,  # Установите высоту, чтобы активировать прокрутку
                ),
                ],
            spacing=10,
            expand=True
        )

        return layout


