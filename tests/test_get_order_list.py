import pytest
import allure
from list_of_orders_methods import ListOfOrderMethods


class TestGetOrdersList:
    @allure.title("Проверка получения списка заказов")
    def test_get_orders_list_success(self):
        response = ListOfOrderMethods.get_orders_list()
        with allure.step('Проверка ответа статус-кода'):
            assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}"

        with allure.step('Проверка, что тело ответа содержит ключ "orders"'):
            response_json = response.json()
            assert "orders" in response_json, "В ответе отсутствует ключ 'orders'"

        with allure.step('Проверка, что "orders" — это список'):
            assert isinstance(response_json["orders"], list)