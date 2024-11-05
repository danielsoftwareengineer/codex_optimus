import pytest
from api.palindrome_api import PalindromeAPI

# Инициализируем API клиент для всех тестов
@pytest.fixture(scope="module")
def api_client():
    return PalindromeAPI()

def test_generate_palindrome(api_client):
    # Генерация строки, которая должна быть палиндромом
    response = api_client.generate_string(palindrome=True)
    assert "id" in response
    assert "result" in response
    result = response["result"]
    assert result == result[::-1]  # Проверка, что строка является палиндромом

def test_generate_non_palindrome(api_client):
    # Генерация строки, которая не должна быть палиндромом
    response = api_client.generate_string(palindrome=False)
    assert "id" in response
    assert "result" in response
    result = response["result"]
    assert result != result[::-1]  # Проверка, что строка не является палиндромом

def test_get_result_found(api_client):
    # Сначала создаём строку
    post_response = api_client.generate_string(palindrome=True)
    string_id = post_response["id"]

    # Затем получаем её по ID
    get_response = api_client.get_result(string_id)
    assert get_response is not None
    assert get_response["id"] == string_id
    assert get_response["result"] == post_response["result"]

def test_get_result_not_found(api_client):
    # Пробуем получить строку с несуществующим ID
    get_response = api_client.get_result("nonexistent-id")
    assert get_response is None  # Проверяем, что ответ — None, т.е. ресурс не найден
