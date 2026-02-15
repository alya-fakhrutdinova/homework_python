from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

wait = WebDriverWait(driver, 40)

wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, 'img')) >= 3)

images = driver.find_elements(By.CSS_SELECTOR, 'img')
img3 = images[2]
print(img3.get_attribute('src'))

driver.quit()
