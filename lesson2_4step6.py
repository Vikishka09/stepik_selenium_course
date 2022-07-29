from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/cats.html")
    browser.find_element(By.ID, "button")


finally:
    time.sleep(10)
    browser.quit()