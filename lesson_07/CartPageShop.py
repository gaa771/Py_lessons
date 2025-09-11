from selenium.webdriver.common.by import By


class CartPageShop:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def open(self):
        self.driver.get(
            "https://www.saucedemo.com/inventory.html"
            )

    def cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
            ).click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"
            ).click()
        self.driver.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link.shopping_cart_link"
            ).click()
