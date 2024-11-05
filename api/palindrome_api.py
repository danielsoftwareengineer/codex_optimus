import requests

class PalindromeAPI:
    def __init__(self, base_url="http://127.0.0.1:8000"):
        self.base_url = base_url

    def generate_string(self, palindrome: bool):
        # Отправляет POST-запрос на генерацию строки
        response = requests.post(f"{self.base_url}/generate", json={"palindrome": palindrome})
        response.raise_for_status()  # Выбрасывает исключение для кода ошибки
        return response.json()  # Возвращает JSON с id и result

    def get_result(self, string_id: str):
        # Отправляет GET-запрос для получения строки по id
        response = requests.get(f"{self.base_url}/result/{string_id}")
        if response.status_code == 404:
            return None  # Если строка не найдена, возвращаем None
        response.raise_for_status()
        return response.json()  # Возвращает JSON с id и result
