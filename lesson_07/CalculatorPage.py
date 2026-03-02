from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
    RESULT_SCREEN = (By.CSS_SELECTOR, ".screen")

    def set_delay(self, value):
        element = self.wait.until(
            EC.element_to_be_clickable(self.DELAY_INPUT)
        )
        element.clear()
        element.send_keys(str(value))

    def click_button_7(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_7)
        )
        button.click()

    def click_plus(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_PLUS)
        )
        button.click()

    def click_button_8(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_8)
        )
        button.click()

    def click_equals(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_EQUALS)
        )
        button.click()

    def get_result(self):
        result_element = self.wait.until(
            EC.visibility_of_element_located(self.RESULT_SCREEN)
        )
        return result_element.text

    def wait_for_result(self, expected_result, timeout=50):
        self.wait.until(
            lambda _: self.get_result() == expected_result
        )