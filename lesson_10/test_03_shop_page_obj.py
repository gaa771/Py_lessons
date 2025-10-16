import pytest
import allure
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


@allure.epic("Тестирование магазина")
@allure.title("Проверка покупки конкретных товаров")
@allure.description("Проверка работоспособности магазина")
@allure.feature("Проверка выполнения ТЗ")
@allure.severity("blocker")
def test_shop(driver):
    with allure.step("Авторизация в магазине"):
        shop_page = AutorizPageShop(driver)
        shop_page.open()
        shop_page.autoriz()
    with allure.step("Добавление четырех товаров в корзину"):
        shop_page = CartPageShop(driver)
        shop_page.open()
        shop_page.cart()
    with allure.step("Нажатие кнопки checkout"):
        shop_page = CheckoutPageShop(driver)
        shop_page.open()
        shop_page.checkout()
    with allure.step("Заполнение формы данными покупателя"):
        shop_page = SwagPageShop(driver)
        shop_page.open()
        shop_page.swag()
    with allure.step("Вычисление суммы покупки"):
        shop_page = ResultPageShop(driver)
        shop_page.open()
        total = shop_page.result()
    with allure.step("Проверка корректности вычисления суммы покупки"):
        assert total == "Total: $58.29"
