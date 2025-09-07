from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/"
                         "selenium-webdriver-java/slow-calculator.html")
        self._driver.maximize_window()

    def input_delay(self):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    def input_keys(self):
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()

    def wait_delay(self):
        WebDriverWait(self._driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))
            )

    def wait_result(self):
        WebDriverWait(self._driver, 60).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15"
            ))

    def res(self):
        res = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        return res
