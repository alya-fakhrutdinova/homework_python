from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def enter_username(self, username):
        element = self.wait.until(
            EC.element_to_be_clickable(self.USERNAME_INPUT)
        )
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        element = self.wait.until(
            EC.element_to_be_clickable(self.PASSWORD_INPUT)
        )
        element.clear()
        element.send_keys(password)

    def click_login(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        button.click()