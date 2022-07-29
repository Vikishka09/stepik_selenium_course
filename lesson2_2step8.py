from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    browser.find_element(By.CSS_SELECTOR, "div > input[name = 'firstname']").send_keys("Vika")
    browser.find_element(By.CSS_SELECTOR, "div > input[name = 'lastname']").send_keys("Pika")
    browser.find_element(By.CSS_SELECTOR, "div > input[name = 'email']").send_keys("vikipiki@gmail.com")
    choice_file = browser.find_element(By.CSS_SELECTOR, "#file")
    choice_file.send_keys("C:\\Users\\Виктория\\selenium_course\\strange_task.txt")
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()

finally:
    time.sleep(10)
    browser.quit()