import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()



def test_slow_calculator(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    wait = WebDriverWait(browser, 60)

    delay_input = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay"))
    )
    delay_input.clear()
    delay_input.send_keys("45")

    button_7 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='7']"))
    )
    button_7.click()

    button_plus = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='+']"))
    )
    button_plus.click()

    button_8 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='8']"))
    )
    button_8.click()

    button_equals = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()=\"=\"]"))
    )
    button_equals.click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15"
        ),
        message="Ожидаемое значение '15' не появилось в поле результата"
    )

    result_element = browser.find_element(By.CSS_SELECTOR, ".screen")
    actual_result = result_element.text

    assert actual_result == "15", f"Ожидаемый результат: 15, фактический: {actual_result}"

    print("Тест пройден успешно: результат вычисления равен 15")