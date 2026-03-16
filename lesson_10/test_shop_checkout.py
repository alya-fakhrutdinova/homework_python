import allure
import pytest
from selenium import webdriver
from .LoginPage import LoginPage
from .MainPage import MainPage
from .CartPage import CartPage
from .CheckoutPage import CheckoutPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации WebDriver.

    Yields:
        WebDriver: Инициализированный экземпляр драйвера браузера.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Оформление заказа в интернет‑магазине")
@allure.story("Полный сценарий покупки товаров")
class TestShopCheckout:

    @allure.title("Успешное оформление заказа с несколькими товарами")
    @allure.description(
        "Проверяет полный сценарий покупки: авторизация → добавление товаров в корзину → "
        "переход в корзину → оформление заказа → проверка итоговой суммы"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_checkout_with_multiple_items(self, driver):
        """
        Тест успешного оформления заказа с несколькими товарами.

        Args:
            driver: Экземпляр WebDriver, предоставляемый фикстурой.
        """
        # Инициализация страниц
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        with allure.step("Открываем страницу авторизации"):
            driver.get("https://www.saucedemo.com/")

        with allure.step("Авторизуемся в системе с валидными учётными данными"):
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")
            login_page.click_login()

        with allure.step("Добавляем товары в корзину"):
            main_page.add_backpack_to_cart()
            main_page.add_bolt_tshirt_to_cart()
            main_page.add_onesie_to_cart()

        with allure.step("Переходим в корзину для проверки товаров"):
            main_page.go_to_cart()

        with allure.step("Нажимаем кнопку оформления заказа"):
            cart_page.click_checkout()

        with allure.step("Заполняем информацию для оформления заказа"):
            checkout_page.enter_first_name("Алия")
            checkout_page.enter_last_name("Фахрутдинова")
            checkout_page.enter_postal_code("443109")

        with allure.step("Продолжаем оформление заказа"):
            checkout_page.click_continue()

        with allure.step("Получаем итоговую сумму заказа"):
            total = checkout_page.get_total_amount()

        with allure.step(f"Проверяем, что итоговая сумма корректна. Ожидаемая: $58.29, фактическая: ${total}"):
            assert abs(total - 58.29) < 0.01, \
                f"Ожидаемая сумма: $58.29, фактическая: ${total}"

    @allure.title("Проверка оформления заказа с одним товаром")
    @allure.description("Проверяет сценарий покупки одного товара")
    @allure.severity(allure.severity_level.NORMAL)
    def test_checkout_single_item(self, driver):
        """
        Тест оформления заказа с одним товаром.

        Args:
            driver: Экземпляр WebDriver, предоставляемый фикстурой.
        """
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        with allure.step("Открываем страницу авторизации"):
            driver.get("https://www.saucedemo.com/")

        with allure.step("Авторизуемся в системе"):
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")
            login_page.click_login()

        with allure.step("Добавляем только рюкзак в корзину"):
            main_page.add_backpack_to_cart()

        with allure.step("Переходим в корзину"):
            main_page.go_to_cart()

        with allure.step("Начинаем оформление заказа"):
            cart_page.click_checkout()

        with allure.step("Заполняем данные для оформления"):
            checkout_page.enter_first_name("Алия")
            checkout_page.enter_last_name("Фахрутдинова")
            checkout_page.enter_postal_code("443109")

        with allure.step("Продолжаем оформление"):
            checkout_page.click_continue()
