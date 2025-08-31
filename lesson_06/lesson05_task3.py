from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# переход на страницу:
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# ожидание выполнения условий:
WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#award")))

# текст элемента и вывод его в терминал
find = driver.find_element(By.CSS_SELECTOR, "#award")
f = find.get_attribute('src')
print(f)

# Закрыть браузер (метод quit()).
driver.quit()
