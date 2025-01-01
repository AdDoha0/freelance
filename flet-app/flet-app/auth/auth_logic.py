import requests



API_URL = "http://127.0.0.1:8000/api"   # Замените на ваш API URL

class Auth:
    def __init__(self):
        self.token = None  # Переменная для хранения токена


    def registration(self, username, password):
        data = {
                "username": username,
                "password":  password
            }
        response = requests.post(f"{API_URL}/auth/users/", json=data)

        print(f"Отправленный запрос: {data}")  # Отладка
        print(f"Статус ответа: {response.status_code}")  # Отладка
        print(f"Ответ сервера: {response.json()}")  # Отладка


        if response.status_code == 201:
            print("Успешаная регистрация, класс Auth")
            print(data)
            return True
        else:
            # Обработка ошибок
            error_message = response.json().get("message", "Неизвестная ошибка")
            print(f"Ошибка регистрации: {error_message}")  # Вывод ошибки
            return False


    def login(self, login, password):
        data = {
                "username": login,
                "password": password
            }
        response = requests.post(f"{API_URL}/token/", json=data)

        if response.status_code == 200:
            print("Успешный вход class Auth")
            self.token = response.json().get("access")  # Сохранение токена
            print(f"token: {self.token}")
            return True  # Успешный вход
        else:
            # Обработка ошибок
            error_message = response.json().get("message", "Неизвестная ошибка")
            return False  # Ошибка входа


    def is_authenticated(self):
        return self.token is not None

    def get_token(self):
        return self.token