from selenium.webdriver.common.by import By


class CheckoutPageShop:
    """
    Класс кнопки Checkout
    """
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def open(self):
        """
        Открытие страницы с кнопкой Checkout
        """
        self.driver.get("https://www.saucedemo.com/cart.html")

    def checkout(self):
        """
        Нажатие кнопки Checkout
        """
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
