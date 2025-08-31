from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(20)

# открыть сайт
driver.get("http://uitestingplayground.com/textinput")

# Найти поле ввода
text_field = "input[type='text']"
text_input = driver.find_element(By.CSS_SELECTOR, text_field)

# Ввести в поле текст SkyPro.
text_input.send_keys("SkyPro")

# Нажать кнопку.
text_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
text_button.click()

# читается: найди текст элемента и выведи его в терминал
print(driver.find_element(By.CSS_SELECTOR, "#updatingButton").text)

# Закрыть браузер (метод quit()).
driver.quit()
