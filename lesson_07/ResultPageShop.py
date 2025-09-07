from selenium.webdriver.common.by import By


class ResultPageShop:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/checkout-step-two.html")
        self._driver.maximize_window()

    def result(self):
        sum = self._driver.find_element(
            By.CSS_SELECTOR, "[data-test='total-label']"
            ).text
        return sum
