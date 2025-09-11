from selenium.webdriver.common.by import By


class ResultPageShop:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def open(self):
        self.driver.get(
            "https://www.saucedemo.com/checkout-step-two.html"
            )

    def result(self):
        total = self.driver.find_element(
            By.CSS_SELECTOR, "[data-test='total-label']"
            ).text
        return total
