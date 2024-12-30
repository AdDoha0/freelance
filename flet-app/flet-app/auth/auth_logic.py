import requests



API_URL = "http://127.0.0.1:8000/api"   # Замените на ваш API URL

class Auth:
    def __init__(self):
        self.token = None  # Переменная для хранения токена


    def login(self, login, password):
        data = {
                "login": login,
                "password": password
            }
        response = requests.post(f"{API_URL}/token/", json=data)

        if response.status_code == 200:
            print("Успешный вход")
            self.token = response.json().get("access")  # Сохранение токена
            return True  # Успешный вход
        else:
            # Обработка ошибок
            error_message = response.json().get("message", "Неизвестная ошибка")
            return False  # Ошибка входа


    def is_authenticated(self):
        return self.token is not None

    def get_token(self):
        return self.token