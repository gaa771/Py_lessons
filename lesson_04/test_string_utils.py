import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# Проверка функции capitalize
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123", "123"),
    ("", ""),
    ("   ", "   "),
    (None, "Error")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Проверка функции trim
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  skypro", "skypro"),
    ("  hello world", "hello world"),
    ("  123", "123"),
    ("python", "python")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", ""),
    (None, "Error")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# Проверка функции contains
@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("skypro", "s", True),
    ("skypro", "u", False),
    ("hello world", "d", True),
    ("hello world", "u", False),
    ("123", "2", True),
    ("123", "u", False)
])
def test_contains_positive(input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("", "", True),
    ("", "f", False),
    (" ", " ", True),
    ("python", " ", False),
    ("python", "python", True),
    ("python", "pn", False),
    (None, "n", "Error"),
    ("SkyPro", None, "Error")
])
def test_contains_negative(input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


# Проверка функции delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("skypro", "s", "kypro"),
    ("skypro", "u", "skypro"),
    ("hello world", "d", "hello worl"),
    ("python", "py", "thon"),
    ("123", "2", "13")
])
def test_delete_symbol_positive(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("", "", ""),
    ("", "f", ""),
    (" ", " ", ""),
    ("python", " ", "python"),
    (None, "n", "Error"),
    ("SkyPro", None, "Error")
])
def test_delete_symbol_negative(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected
