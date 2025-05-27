import pytest
import allure

from create_order_methods import CreateOrderMethods
from generators import generate_create_order_body


class TestCreateOrder:
    @allure.title("Проверка создания заказа с разными параметрами цвета")
    @pytest.mark.parametrize("color", [
        (["BLACK"]),
        (["GREY"]),
        (["BLACK", "GREY"]),
        ([])
    ])
    def test_create_order_with_different_colors(self, color):
        order_body = generate_create_order_body()
        order_body["color"] = color

        response = CreateOrderMethods.create_order(order_body)

        assert response.status_code == 201, f"Ожидался статус 201, но был {response.status_code}"
        with allure.step('Проверка, что в теле ответа содержится "track"'):
            assert "track" in response.json(), "Ответ не содержит поле 'track'"