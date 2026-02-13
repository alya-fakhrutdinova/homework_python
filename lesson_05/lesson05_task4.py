from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.maximize_window()
driver.get('http://the-internet.herokuapp.com/login')

name = '#username'
name_input = driver.find_element(By.CSS_SELECTOR, name)
name_input.send_keys('tomsmith')

password = '#password'
password_input = driver.find_element(By.CSS_SELECTOR, password)
password_input.send_keys('SuperSecretPassword!')

login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
login_button.click()

success_alert = driver.find_element(By.CSS_SELECTOR, '.flash.success')

alert_text = success_alert.text
print('Текст с зелёной плашки:')
print(alert_text)


sleep(3)
driver.quit()