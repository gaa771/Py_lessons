import pytest
from selenium import webdriver
from CalcPage import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
    yield driver
    driver.quit()


def test_calc(driver):
    form_page = CalcPage(driver)
    form_page.input_delay()
    form_page.input_keys()
    form_page.wait_delay()
    form_page.wait_result()
    result = form_page.res()

    assert result == "15"
