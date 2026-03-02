import pytest
from selenium import webdriver
from CalculatorPage import CalculatorPage



def test_calculator_functionality():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    calculator = CalculatorPage(driver)

    calculator.set_delay(45)

    calculator.click_button_7()
    calculator.click_plus()
    calculator.click_button_8()
    calculator.click_equals()

    calculator.wait_for_result("15")

    result = calculator.get_result()
    assert result == "15", f"Ожидаемый результат: 15, фактический: {result}"

    driver.quit()