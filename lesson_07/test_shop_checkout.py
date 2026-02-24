import pytest
from selenium import webdriver
from LoginPage import LoginPage
from MainPage import MainPage
from CartPage import CartPage
from CheckoutPage import CheckoutPage



def test_shop_checkout():
    driver = webdriver.Firefox()
    driver.maximize_window()

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    inventory_page = MainPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    inventory_page.add_backpack_to_cart()
    inventory_page.add_bolt_tshirt_to_cart()
    inventory_page.add_onesie_to_cart()
    inventory_page.go_to_cart()

    cart_page.click_checkout()

    checkout_page.enter_first_name("Алия")
    checkout_page.enter_last_name("Фахрутдинова")
    checkout_page.enter_postal_code("443109")
    checkout_page.click_continue()

    total = checkout_page.get_total_amount()
    assert total == 58.29, f"Ожидаемая сумма: $58.29, фактическая: ${total}"

    driver.quit()