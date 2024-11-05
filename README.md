# Тестовое API для генерации строк

## Описание

Данный проект реализует REST API на FastAPI для генерации строк. API поддерживает два эндпоинта:

	1.	POST /generate — генерирует строку, которая может быть либо палиндромом, либо произвольной строкой.
	2.	GET /result/{id} — возвращает строку, сгенерированную ранее по ее id.

Проект также включает автотесты для проверки работы API, написанные с использованием pytest и requests, с применением паттерна Page Object Model (POM) для организации тестов.

## Установка и запуск

1. Клонируйте репозиторий и перейдите в директорию проекта:
   ```bash
   git clone <URL репозитория>
   cd palindrome-api

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt

3. Запустите FastAPI приложение:
   ```bash
   uvicorn main:app --reload

Приложение будет доступно по адресу http://127.0.0.1:8000.

## Эндпоинты API

1. POST /generate

 	•	Описание: Генерирует строку на основе параметра palindrome.

 	•	Параметры: palindrome (boolean) — если True, сгенерированная строка будет палиндромом. Если False, строка будет произвольной и не будет палиндромом.
	
 	•	Пример запроса:

		{
			"palindrome": true
	   	}


 	•	Пример ответа:

	   	{
			"id": "550e8400-e29b-41d4-a716-446655440000",
			"result": "racecar"
		}

2. GET /result/{id}

 	•	Описание: Возвращает строку по её id.

	•	Параметры:
	•	    id (UUID) — идентификатор ранее сгенерированной строки.

 	•	Пример запроса:

		GET /result/550e8400-e29b-41d4-a716-446655440000

 	•	Пример ответа:

	 	{
		    "id": "550e8400-e29b-41d4-a716-446655440000",
		    "result": "racecar"
		}

# Тестирование 

Для тестирования API используется pytest вместе с библиотекой requests и паттерном Page Object Model (POM), который структурирует взаимодействие с API.

## Структура проекта

Проект включает следующие файлы:

 	•	main.py — реализация API на FastAPI.
 
	•	api/palindrome_api.py — класс PalindromeAPI, реализующий Page Object Model для работы с эндпоинтами API.
 
	•	test_main.py — тесты для проверки работы API, использующие PalindromeAPI для взаимодействия с сервером.
 
	•	api/__init__.py — файл инициализации, упрощающий импорт класса PalindromeAPI.

## Структура Page Object Model

Класс PalindromeAPI в файле api/palindrome_api.py предоставляет методы для работы с эндпоинтами API:

	•	generate_string(palindrome: bool) — отправляет запрос на генерацию строки с параметром palindrome.
 
	•	get_result(string_id: str) — отправляет запрос на получение строки по её id.
 

## Запуск тестов

1.	Убедитесь, что сервер FastAPI запущен по адресу http://127.0.0.1:8000.
2.	Запустите тесты с помощью команды:
	   ```bash
	   pytest test_main.py

## Описание тестов

Файл test_main.py содержит следующие тесты:

	•	test_generate_palindrome — проверяет генерацию палиндрома (параметр palindrome=True).
 
	•	test_generate_non_palindrome — проверяет генерацию непалиндромной строки (параметр palindrome=False).
 
	•	test_get_result_found — проверяет, что сгенерированная строка успешно возвращается по её id.
 
	•	test_get_result_not_found — проверяет обработку запроса с несуществующим id.
 

## Пример использования Page Object Model в тестах

В файле test_main.py используется объект PalindromeAPI для выполнения запросов. Пример:

	from api import PalindromeAPI
	
	@pytest.fixture(scope="module")
	def api_client():
	    return PalindromeAPI()
	
	def test_generate_palindrome(api_client):
	    response = api_client.generate_string(palindrome=True)
	    assert "id" in response
	    assert response["result"] == response["result"][::-1]  # Проверка на палиндром


# Тестовое API для генерации строк

Данный проект предоставляет REST API для генерации и получения строк с поддержкой палиндромов. Тесты, написанные с использованием pytest, демонстрируют базовую верификацию работы API, а применение паттерна Page Object Model улучшает читаемость и структуру кода тестов.
