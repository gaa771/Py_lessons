from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

# открыть сайт
driver.get("http://the-internet.herokuapp.com/inputs")

# Найти поле ввода
search_field = "input[type='number']"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)

# Ввести в поле текст Sky.
search_input.send_keys("Sky")

# Очистить это поле (метод clear()).
search_input.clear()

# Ввести в поле текст Pro.
search_input.send_keys("Pro")

# Закрыть браузер (метод quit()).
driver.quit()
