from selenium.webdriver.common.by import By


class CheckoutPageShop:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def open(self):
        self.driver.get(
            "https://www.saucedemo.com/cart.html"
            )

    def checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
