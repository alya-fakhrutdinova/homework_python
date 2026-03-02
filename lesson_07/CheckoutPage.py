from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def enter_first_name(self, first_name):
        element = self.wait.until(
            EC.element_to_be_clickable(self.FIRST_NAME_INPUT)
        )
        element.clear()
        element.send_keys(first_name)

    def enter_last_name(self, last_name):
        element = self.wait.until(
            EC.element_to_be_clickable(self.LAST_NAME_INPUT)
        )
        element.clear()
        element.send_keys(last_name)

    def enter_postal_code(self, postal_code):
        element = self.wait.until(
            EC.element_to_be_clickable(self.POSTAL_CODE_INPUT)
        )
        element.clear()
        element.send_keys(postal_code)

    def click_continue(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        button.click()

    def get_total_amount(self):
        total_element = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_LABEL)
        )
        total_text = total_element.text
        return float(total_text.replace("Total: $", ""))