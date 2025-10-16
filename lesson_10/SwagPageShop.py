from selenium.webdriver.common.by import By


class SwagPageShop:
    """
    Класс страницы формы покупателя
    """
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def open(self):
        """
        Открытие страницы формы покупателя
        """
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")

    def swag(self) -> str:
        """
        Заполнение формы покупателя.
        Расчет итоговой суммы
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys("Голубцов")
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys("Артем")
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys("301470")
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
        total = self.driver.find_element(
            By.CSS_SELECTOR, "[data-test='total-label']").text
        return total
