import allure
import pytest
from selenium import webdriver
from .CalculatorPage import CalculatorPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.feature("Калькулятор")
@allure.story("Базовые вычисления")
class TestCalculator:

    @allure.title("Тест сложения 7 + 8")
    @allure.description("Проверяет, что калькулятор правильно складывает 7 и 8")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_calculator_functionality(self, driver):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        calculator = CalculatorPage(driver)

        with allure.step("Устанавливаем задержку 45 мс"):
            calculator.set_delay(45)

        with allure.step("Нажимаем кнопки: 7, +, 8, ="):
            calculator.click_button_7()
            calculator.click_plus()
            calculator.click_button_8()
            calculator.click_equals()

        with allure.step("Ожидаем результат 15"):
            calculator.wait_for_result("15")

        with allure.step("Проверяем, что результат равен 15"):
            result = calculator.get_result()
            assert result == "15", f"Ожидаемый результат: 15, фактический: {result}"
