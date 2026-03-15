from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Union

class CalculatorPage:
    """
    Page Object для страницы калькулятора.
    """

    def __init__(self, driver) -> None:
        """
        Инициализация страницы калькулятора.

        Args:
            driver: WebDriver экземпляр.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
    RESULT_SCREEN = (By.CSS_SELECTOR, ".screen")

    def set_delay(self, value: Union[int, str]) -> None:
        """
        Устанавливает задержку в калькуляторе.

        Args:
            value (int | str): Значение задержки в миллисекундах.
        """
        element = self.wait.until(
            EC.element_to_be_clickable(self.DELAY_INPUT)
        )
        element.clear()
        element.send_keys(str(value))

    def click_button_7(self) -> None:
        """
        Кликает на кнопку '7' на калькуляторе.
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_7)
        )
        button.click()

    def click_plus(self) -> None:
        """
        Кликает на кнопку '+' (сложение) на калькуляторе.
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_PLUS)
        )
        button.click()

    def click_button_8(self) -> None:
        """
        Кликает на кнопку '8' на калькуляторе.
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_8)
        )
        button.click()

    def click_equals(self) -> None:
        """
        Кликает на кнопку '=' (равно) на калькуляторе для получения результата.
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_EQUALS)
        )
        button.click()

    def get_result(self) -> str:
        """
        Получает текущий результат вычисления с экрана калькулятора.

        Returns:
            str: Текст результата, отображаемый на экране калькулятора.
        """
        result_element = self.wait.until(
            EC.visibility_of_element_located(self.RESULT_SCREEN)
        )
        return result_element.text

    def wait_for_result(self, expected_result: str, timeout: int = 50) -> None:
        """
        Ожидает появления ожидаемого результата на экране калькулятора.

        Args:
            expected_result (str): Ожидаемый результат вычисления.
            timeout (int): Максимальное время ожидания в секундах (по умолчанию 50).
        """
        self.wait.until(
            lambda _: self.get_result() == expected_result
        )
