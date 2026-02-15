from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru/")
driver.maximize_window() #развернуть окно под размер экрана
driver.set_window_size(1000, 600)
driver.minimize_window() #свернуть окно
driver.fullscreen_window()

sleep(10)
driver.quit()