import pytest
import allure
from selenium import webdriver
from CalcPage import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.epic("Тестирование калькулятора")
@allure.title("Проверка расчета конкретного выражения")
@allure.description("Проверка работоспособности калькулятора")
@allure.feature("Проверка выполнения ТЗ")
@allure.severity("blocker")
def test_calc(driver):
    calc_page = CalcPage(driver)
    with allure.step("Открытие страницы"):
        calc_page.open()
    with allure.step("Установка задержки 45 секунд"):
        calc_page.input_delay()
    with allure.step("Ввод данных для вычисления"):
        calc_page.input_keys()
    with allure.step("Ожидание результата"):
        calc_page.wait_result()
        result = calc_page.res()
    with allure.step("Проверка корректности вычисления суммы"):
        assert result == "15"
