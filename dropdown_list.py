from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
# import math


# link = "http://suninjuly.github.io/simple_form_find_task.html"
# link = "http://suninjuly.github.io/find_link_text"
link_XPATH = " https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link_XPATH)
    # m = str(math.ceil(math.pow(math.pi, math.e)*10000))
    # link = browser.find_element(By.PARTIAL_LINK_TEXT, m)
    # link.click()
    browser.execute_script("document.title = 'Abkhazia'; alert('Robots work');")
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")

    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")

    sum = int(num1.text)+int(num2.text)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))

    browser.find_element(By.CSS_SELECTOR, "[type=submit].btn.btn-default").click()

finally:

    time.sleep(9)

    browser.quit()
