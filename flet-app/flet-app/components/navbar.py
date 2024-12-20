import flet as ft

def create_navbar() -> ft.Row:
    # Создание навигационного бара внизу экрана
    navbar = ft.Row(
        controls=[
            ft.IconButton(ft.icons.HOME, tooltip="Главная", icon_color="#B2FF66"),
            ft.IconButton(ft.icons.STAR, tooltip="Избранное", icon_color="#B2FF66"),
            ft.IconButton(ft.icons.INFO, tooltip="О нас", icon_color="#B2FF66"),
            ft.IconButton(ft.icons.CONTACT_MAIL, tooltip="Контакты", icon_color="#B2FF66"),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Обернем Row в Container для изменения стиля
    return ft.Container(
        content=navbar,
        bgcolor="#1A1A2E",
        padding=ft.padding.only(top=7, bottom=7),  # Установка отступов только сверху и снизу
        margin=ft.margin.only(left=0, right=0),  # Установка отступов для контейнера
    )

# def create_search_box():

#     # Поисковая строка
#     search_box = ft.TextField(label="Поиск проектов", width=400)
#     search_button = ft.ElevatedButton("Поиск", on_click=lambda e: search_projects(search_box.value))

#     # results_container = ft.Column()

#     def search_projects(query):
#         # Логика поиска проектов
#         print(f"Поиск проектов по запросу: {query}")

#         # Очистка предыдущих результатов
#         # results_container.controls.clear()

#     return ft.Container(
#         content=(
#             ft.Column(
#                 search_box,
#                 search_button
#                 )
#             )
#         )




#vkvfkmmv
# bgcolor=ft.colors.TRANSPARENT, color=ft.colors.LIGHT_GREEN