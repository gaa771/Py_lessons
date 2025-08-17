from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

# открыть сайт
driver.get("http://the-internet.herokuapp.com/login")

# В поле username ввести значение tomsmith.
username_field = "input[id='username']"
username_input = driver.find_element(By.CSS_SELECTOR, username_field)
username_input.send_keys("tomsmith")

# В поле password ввести значение SuperSecretPassword!.
password_field = "input[id='password']"
password_input = driver.find_element(By.CSS_SELECTOR, password_field)
password_input.send_keys("SuperSecretPassword!")

# Нажать кнопку Login.
login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()

# Вывести текст с зеленой плашки в консоль.
green_text = driver.find_element(By.CSS_SELECTOR, "#flash.flash.success").text
print(green_text)

# Закрыть браузер (метод quit()).
driver.quit()
