from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """
    Page Object для страницы авторизации.
    """

    def __init__(self, driver) -> None:
        """
        Инициализация страницы авторизации.

        Args:
            driver: WebDriver экземпляр.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя в поле логина.

        Args:
            username (str): Имя пользователя для авторизации.

        Raises:
            TimeoutException: Если поле ввода имени пользователя не становится
                кликабельным в течение заданного времени ожидания.
        """
        element = self.wait.until(
            EC.element_to_be_clickable(self.USERNAME_INPUT)
        )
        element.clear()
        element.send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Вводит пароль в соответствующее поле.

        Args:
            password (str): Пароль пользователя для авторизации.

        Raises:
            TimeoutException: Если поле ввода пароля не становится кликабельным
                в течение заданного времени ожидания.
        """
        element = self.wait.until(
            EC.element_to_be_clickable(self.PASSWORD_INPUT)
        )
        element.clear()
        element.send_keys(password)

    def click_login(self) -> None:
        """
        Кликает на кнопку входа в систему.

        Raises:
            TimeoutException: Если кнопка входа не становится кликабельным
                в течение заданного времени ожидания.
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        button.click()
