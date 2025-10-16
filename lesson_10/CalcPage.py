from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    """
    Класс страницы калькулятора
    """
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def open(self):
        """
        Открытие страницы калькулятора
        """
        self.driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html")

    def input_delay(self):
        """
        Установка времени задержки 45 секунд
        """
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    def input_keys(self):
        """
        Ввод слагаемых и вычисление результата
        """
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()

    def wait_result(self):
        """
        Ожидание появления результата
        """
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15"))

    def res(self) -> str:
        """
        Возврат результата вычисления
        """
        res = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return res
