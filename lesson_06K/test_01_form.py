
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    yield driver
    driver.quit()


def test_01_form(driver):
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.implicitly_wait(5)
    driver.find_element(
        By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3").click()

    input_field_zip = driver.find_element(
        By.CSS_SELECTOR, "#zip-code").get_attribute("class")
    assert input_field_zip == "alert py-2 alert-danger"

    input_fields = ["#first-name", "#last-name", "#address",
                    "#city", "#country", "#e-mail", "#phone", "#company"]
    for input_field in input_fields:
        input_field_class = driver.find_element(
            By.CSS_SELECTOR, input_field).get_attribute("class")
        assert input_field_class == "alert py-2 alert-success"

    driver.implicitly_wait(5)
    driver.quit()
