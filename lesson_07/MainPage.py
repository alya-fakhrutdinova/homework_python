from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class MainPage:
    def __init__(self, driver):
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

    def add_backpack_to_cart(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.BACKPACK_ADD_BUTTON)
        )
        button.click()

    def add_bolt_tshirt_to_cart(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.BOLT_TSHIRT_ADD_BUTTON)
        )
        button.click()

    def add_onesie_to_cart(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.ONESIE_ADD_BUTTON)
        )
        button.click()

    def go_to_cart(self):
        link = self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        )
        link.click()