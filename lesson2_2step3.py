from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects2.html")

    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    x = x_element.text
    y = y_element.text
    z = str(int(x) + int(y))

    select = Select(browser.find_element(By.TAG_NAME, "select"))  # найти элемент список и кликнуть
    select.select_by_value(z)  # ищем элемент со значением суммы
    browser.find_element(By.CSS_SELECTOR, ".btn-default").click()

finally:
    time.sleep(10)
    browser.quit()