from selenium.webdriver.common.by import By


class AutorizPageShop:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def open(self):
        self.driver.get(
            "https://www.saucedemo.com/"
            )

    def autoriz(self):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").clear()
        self.driver.find_element(
            By.CSS_SELECTOR, "#user-name"
            ).send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").clear()
        self.driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
