from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.maximize_window()
driver.get('http://the-internet.herokuapp.com/inputs')

search_field = 'input'
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys('Sky')
sleep(5)
search_input.clear()
sleep(5)
search_input.send_keys('Pro')
sleep(5)
driver.quit()
