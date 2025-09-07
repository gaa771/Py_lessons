import pytest
from selenium import webdriver
from AutorizPageShop import AutorizPageShop
from CartPageShop import CartPageShop
from CheckoutPageShop import CheckoutPageShop
from SwagPageShop import SwagPageShop
from ResultPageShop import ResultPageShop


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shop(driver):
    form_page = AutorizPageShop(driver)
    form_page.autoriz()
    form_page = CartPageShop(driver)
    form_page.cart()
    form_page = CheckoutPageShop(driver)
    form_page.checkout()
    form_page = SwagPageShop(driver)
    form_page.swag()
    form_page = ResultPageShop(driver)
    sum = form_page.result()
    assert sum == "Total: $58.29"
