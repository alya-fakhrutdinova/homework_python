from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Union

class CheckoutPage:
    """
    Page Object для страницы оформления заказа.
    """

    def __init__(self, driver) -> None:
        """
        Инициализация страницы оформления заказа.

        Args:
            driver: WebDriver экземпляр.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def enter_first_name(self, first_name: str) -> None:
        """
        Вводит имя пользователя в соответствующее поле на странице оформления заказа.

        Args:
            first_name (str): Имя пользователя, которое будет введено в поле.

        Raises:
            TimeoutException: Если поле ввода имени не становится кликабельным
                в течение заданного времени ожидания.
        """
        element = self.wait.until(
            EC.element_to_be_clickable(self.FIRST_NAME_INPUT)
        )
        element.clear()
        element.send_keys(first_name)

    def enter_last_name(self, last_name: str) -> None:
        """
        Вводит фамилию пользователя в соответствующее поле на странице оформления заказа.

        Args:
            last_name (str): Фамилия пользователя, которая будет введена в поле.

        Raises:
            TimeoutException: Если поле ввода фамилии не становится кликабельным
                в течение заданного времени ожидания.
        """
        element = self.wait.until(
            EC.element_to_be_clickable(self.LAST_NAME_INPUT)
        )
        element.clear()
        element.send_keys(last_name)

    def enter_postal_code(self, postal_code: Union[str, int]) -> None:
        """
        Вводит почтовый индекс в соответствующее поле на странице оформления заказа.

        Args:
            postal_code (str | int): Почтовый индекс. Может быть передан
                как строка или число — будет автоматически преобразован в строку.

        Raises:
            TimeoutException: Если поле ввода почтового индекса не становится
                кликабельным в течение заданного времени ожидания.
        """
        element = self.wait.until(
            EC.element_to_be_clickable(self.POSTAL_CODE_INPUT)
        )
        element.clear()
        element.send_keys(str(postal_code))

    def click_continue(self) -> None:
        """
        Кликает на кнопку продолжения оформления заказа.

        Raises:
            TimeoutException: Если кнопка продолжения не становится кликабельной
                в течение заданного времени ожидания.
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        button.click()

    def get_total_amount(self) -> float:
        """
        Получает общую сумму заказа из соответствующего элемента на странице.

        Returns:
            float: Общая сумма заказа в денежном выражении (например, 58.29).

        Raises:
            TimeoutException: Если элемент с суммой не становится видимым
                в течение заданного времени ожидания.
            ValueError: Если текст элемента не может быть преобразован в число
                (например, если формат отличается от ожидаемого).
        """
        total_element = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_LABEL)
        )
        total_text = total_element.text
        # Удаляем префикс "Total: $" и преобразуем в число
        return float(total_text.replace("Total: $", ""))
