import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()



def test_shop_checkout(browser):
    browser.get("https://www.saucedemo.com/")
    wait = WebDriverWait(browser, 10)

    username_input = wait.until(
        EC.element_to_be_clickable((By.ID, "user-name"))
    )
    username_input.send_keys("standard_user")

    password_input = wait.until(
        EC.element_to_be_clickable((By.ID, "password"))
    )
    password_input.send_keys("secret_sauce")

    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    login_button.click()

    backpack_add_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='inventory_item' and .//div[text()='Sauce Labs Backpack']]//button")
        )
    )
    backpack_add_button.click()

    tshirt_add_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='inventory_item' and .//div[text()='Sauce Labs Bolt T-Shirt']]//button")
        )
    )
    tshirt_add_button.click()

    onesie_add_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='inventory_item' and .//div[text()='Sauce Labs Onesie']]//button")
        )
    )
    onesie_add_button.click()

    cart_badge = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    )
    cart_badge.click()

    checkout_button = wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_button.click()

    first_name_input = wait.until(
        EC.element_to_be_clickable((By.ID, "first-name"))
    )
    first_name_input.send_keys("Алия")

    last_name_input = wait.until(
        EC.element_to_be_clickable((By.ID, "last-name"))
    )
    last_name_input.send_keys("Фахрутдинова")

    postal_code_input = wait.until(
        EC.element_to_be_clickable((By.ID, "postal-code"))
    )
    postal_code_input.send_keys("443109")

    continue_button = wait.until(
        EC.element_to_be_clickable((By.ID, "continue"))
    )
    continue_button.click()

    total_element = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text

    total_amount = float(total_text.replace("Total: $", ""))

    assert total_amount == 58.29, f"Ожидаемая сумма: $58.29, фактическая: ${total_amount}"