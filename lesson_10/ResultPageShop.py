from selenium.webdriver.common.by import By


class ResultPageShop:
    """
    Класс страницы итогового результата
    """
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def open(self):
        """
        Открытие страницы итогового результата
        """
        self.driver.get("https://www.saucedemo.com/checkout-step-two.html")

    def result(self) -> str:
        """
        Возврат итоговой суммы покупки
        """
        total = self.driver.find_element(
            By.CSS_SELECTOR, "[data-test='total-label']").text
        return total
