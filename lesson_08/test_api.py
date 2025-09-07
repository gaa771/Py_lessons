import requests
import pytest

base_url = 'https://ru.yougile.com/api-v2/projects/'
# Заменить на реальный api_key
api_key = "api_key"
# Заменить на реальный user_id
user_id = "user_id"


# Авторизация
@pytest.fixture
def headers():
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }


# Создание нового проекта перед тестами по обновлению и получению проекта по id
@pytest.fixture
def create_project(headers):
    data = {
        "title": "Домашнее задание 8_2",
        "users": {
            user_id: "admin"
            }
    }
    response = requests.post(
        base_url,
        headers=headers,
        json=data
    )
    assert response.status_code == 201
    return response.json()["id"]


# Позитивный тест создания проекта
def test_create_project_positive(headers):
    data = {
        "title": "Домашнее задание 8",
        "users": {
            user_id: "admin"
            }
    }
    response = requests.post(base_url, headers=headers, json=data)

    assert response.status_code == 201


# Негативный тест создания проекта (пустое название)
def test_create_project_negative(headers):
    data = {
        "title": "",
        "users": {
            user_id: "admin"
            }
    }
    response = requests.post(base_url, headers=headers, json=data)

    assert response.status_code == 400


# Позитивный тест обновления проекта
def test_update_project_positive(create_project, headers):
    project_id = create_project
    data = {"title": "Домашнее задание 8_1"}
    response = requests.put(
        f"{base_url}{project_id}",
        headers=headers,
        json=data
    )
    assert response.status_code == 200


# Негативный тест обновления несуществующего проекта
def test_update_project_negative(headers):
    project_id = "Несуществующий проект"
    data = {"title": "Домашнее задание 8_1"}
    response = requests.put(
        f"{base_url}{project_id}",
        headers=headers,
        json=data
    )
    assert response.status_code == 404


# Позитивный тест получения проекта по id
def test_get_project_positive(create_project, headers):
    project_id = create_project
    response = requests.get(
        f"{base_url}{project_id}",
        headers=headers
    )
    assert response.status_code == 200


# Негативный тест получения проекта по несуществующему id
def test_get_project_negative(headers):
    project_id = "Несуществующий проект"
    response = requests.get(
        f"{base_url}{project_id}",
        headers=headers
    )
    assert response.status_code == 404
