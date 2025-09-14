from selenium.webdriver.common.by import By


class FormPage:
    """
    Класс страницы формы
    """
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def open(self):
        """
        Открытие страницы формы
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def input_data_form(self):
        """
        Ввод данных формы
        """
        self.driver.find_element(By.NAME, "first-name").send_keys("Иван")
        self.driver.find_element(By.NAME, "last-name").send_keys("Петров")
        self.driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        self.driver.find_element(By.NAME, "city").send_keys("Москва")
        self.driver.find_element(By.NAME, "country").send_keys("Россия")
        self.driver.find_element(
            By.NAME, "e-mail").send_keys("test@skypro.com")
        self.driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        self.driver.find_element(By.NAME, "job-position").send_keys("QA")
        self.driver.find_element(By.NAME, "company").send_keys("SkyPro")

        self.driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']").click()
        self.driver.implicitly_wait(5)

    def find_field_zip(self) -> str:
        """
        Поиск поля Zip code (незаполненное поле)
        Возвращает переменную с атрибутом "class"
        """
        input_field_zip = self.driver.find_element(
            By.ID, "zip-code").get_attribute("class")
        return input_field_zip

    def find_field_class(self) -> list:
        """
        Поиск и создание списка остальных заполненных полей
        Возвращает список атрибутов "class"
        """

        input_fields = ["#first-name", "#last-name", "#address",
                        "#city", "#country", "#e-mail", "#phone", "#company"]

        input_field_class_list = list()
        for input_field in input_fields:
            input_field_class = self.driver.find_element(
                By.CSS_SELECTOR, input_field).get_attribute("class")
            input_field_class_list.append(input_field_class)

        return input_field_class_list
