from selenium.webdriver.common.by import By


class SwagPageShop:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/checkout-step-one.html")
        self._driver.maximize_window()

    def swag(self):
        self._driver.find_element(
            By.CSS_SELECTOR, "#first-name"
            ).send_keys("Голубцов")
        self._driver.find_element(
            By.CSS_SELECTOR, "#last-name"
            ).send_keys("Артем")
        self._driver.find_element(
            By.CSS_SELECTOR, "#postal-code"
            ).send_keys("301470")
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()
        sum = self._driver.find_element(
            By.CSS_SELECTOR, "[data-test='total-label']"
            ).text
        return sum
