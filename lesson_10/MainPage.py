from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    """
    Page Object для главной страницы магазина.
    """

    def __init__(self, driver) -> None:
        """
        Инициализация главной страницы.

        Args:
            driver: WebDriver экземпляр.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    BACKPACK_ADD_BUTTON = (
        By.XPATH,
        "//div[@class='inventory_item' and .//div[text()='Sauce Labs Backpack']]//button"
    )
    BOLT_TSHIRT_ADD_BUTTON = (
        By.XPATH,
        "//div[@class='inventory_item' and .//div[text()='Sauce Labs Bolt T-Shirt']]//button"
    )
    ONESIE_ADD_BUTTON = (
        By.XPATH,
        "//div[@class='inventory_item' and .//div[text()='Sauce Labs Onesie']]//button"
    )
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self) -> None:
        """
        Добавляет рюкзак (Sauce Labs Backpack) в корзину.

        Raises:
            TimeoutException: Если кнопка добавления рюкзака не становится кликабельным
                в течение заданного времени ожидания.
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self.BACKPACK_ADD_BUTTON)
        )
        button.click()

    def add_bolt_tshirt_to_cart(self) -> None:
        """
        Добавляет футболку (Sauce Labs Bolt T‑Shirt) в корзину.

        Raises:
            TimeoutException: Если кнопка добавления футболки не становится кликабельным
                в течение заданного времени ожидания.
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self.BOLT_TSHIRT_ADD_BUTTON)
        )
        button.click()

    def add_onesie_to_cart(self) -> None:
        """
        Добавляет комбинезон (Sauce Labs Onesie) в корзину.

        Raises:
            TimeoutException: Если кнопка добавления комбинезона не становится кликабельным
                в течение заданного времени ожидания.
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self.ONESIE_ADD_BUTTON)
        )
        button.click()

    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины, кликая по иконке корзины.

        Raises:
            TimeoutException: Если ссылка на корзину не становится кликабельным
                в течение заданного времени ожидания.
        """
        link = self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        )
        link.click()
