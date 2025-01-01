import requests



API_URL = "http://127.0.0.1:8000/api"   # Замените на ваш API URL

class Auth:
    token = None  # Переменная для хранения токена
    current_user_id = None # id теекущего пользователя


    def registration(self, username, password):
        data = {
                "username": username,
                "password":  password
            }
        response = requests.post(f"{API_URL}/auth/users/", json=data)


        # Отладка
        print(f"Отправленный запрос: {data}")
        print(f"Статус ответа: {response.status_code}")
        print(f"Ответ сервера: {response.json()}")


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
            Auth.token = response.json().get("access")  # Сохранение токена
            print(f"token: {Auth.token}")

            # Получаем информацию о текущем пользователе
            user_info_response = requests.get(f"{API_URL}/auth/users/me/", headers={"Authorization": f"Bearer {Auth.token}"})
            if user_info_response.status_code == 200:
                Auth.current_user_id = user_info_response.json().get("id")  # Сохранение ID пользователя
                print(f"Текущий пользователь ID: {Auth.current_user_id}")
                return True  # Успешный вход
            else:
                print(f"Ошибка получения информации о текущем пользователе: {user_info_response.json()}")
                return False
        else:
            # Обработка ошибок
            error_message = response.json().get("message", "Неизвестная ошибка")
            print(error_message)
            return False  # Ошибка входа


    # def is_authenticated(self):
    #     return self.token is not None

    # def get_token(self):
    #     return self.token