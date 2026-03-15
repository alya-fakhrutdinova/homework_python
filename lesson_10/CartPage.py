from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    """
    Page Object для страницы корзины.
    """

    def __init__(self, driver) -> None:
        """
        Инициализация страницы корзины.

        Args:
            driver: WebDriver экземпляр.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def click_checkout(self) -> None:
        """
        Кликает на кнопку оформления заказа (Checkout) на странице корзины.

        Raises:
            TimeoutException: Если кнопка не становится кликабельной в течение заданного времени ожидания.
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        button.click()
