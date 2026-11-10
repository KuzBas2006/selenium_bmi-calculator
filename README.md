# Автоматизированное тестирование BMI Calculator

Автотесты для калькулятора индекса массы тела (BMI) на сайте calculator.net. 

## Технологии
* Python 3.12
* Pytest
* Selenium WebDriver
* Allure Framework
* Page Object Model (POM)

## Структура проекта
* `pages/` — классы страниц и локаторы (Page Object).
* `tests/` — тестовые сценарии.
* `conftest.py` — настройки браузера (работает в фоновом headless-режиме) и фикстуры.
* `requirements.txt` — список нужных библиотек.

## Как запустить тесты

1. Установите зависимости:
   pip install -r requirements.txt

2. Запустите тесты (отчеты сохранятся в папку allure-results):
   python -m pytest --alluredir=allure-results

3. Откройте графический отчет (нужен Allure CLI):
   allure serve allure-results