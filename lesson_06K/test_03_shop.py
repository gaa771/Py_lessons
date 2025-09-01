import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
        )
    yield driver
    driver.quit()


def test_03_shop(driver):
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.CSS_SELECTOR, "#user-name").clear()
    driver.find_element(
        By.CSS_SELECTOR, "#user-name"
        ).send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").clear()
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"
        ).click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"
        ).click()

    driver.find_element(
        By.CSS_SELECTOR, "a.shopping_cart_link.shopping_cart_link"
        ).click()
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Артем")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Голубцов")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("301470")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    sum = driver.find_element(
        By.CSS_SELECTOR, "[data-test='total-label']"
        ).text

    assert sum == "Total: $58.29"
