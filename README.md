# homework_python

# Домашнее задание №10

## Описание
Проект содержит автоматические тесты для:
- Калькулятора с задержкой (сайт: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html)
- Интернет-магазина (сайт: https://www.saucedemo.com/)
Тесты написаны с использованием PageObject паттерна.

## Установка и запуск тестов

1. Установить зависимости:
   ```bash
   pip install selenium pytest allure-pytest

   Запустить все тесты:
 pytest

    Запустить тесты с сохранением результатов Allure:
lesson_10/ --alluredir=allure-results

  Просмотреть отчет Allure:
allure serve allure-results