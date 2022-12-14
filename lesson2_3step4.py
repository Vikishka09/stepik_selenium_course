from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    confirm = browser.switch_to.alert
    confirm.accept()  # Принять (нажать ок)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()

finally:
    print(browser.switch_to.alert.text)
    time.sleep(10)
    browser.quit()