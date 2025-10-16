from selenium.webdriver.common.by import By


class AutorizPageShop:
    """
    Класс авторизации пользователя магазина
    """
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def open(self):
        """
        Открытие страницы авторизации
        """
        self.driver.get("https://www.saucedemo.com/")

    def autoriz(self):
        """
        Заполнение информации для авторизации на странице магазина
        """
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").clear()
        self.driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").clear()
        self.driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
