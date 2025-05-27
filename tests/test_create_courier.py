import allure

from create_courier_methods import CreateCourierMethods
from generators import generate_create_courier_body


class TestCreateCourier:
    @allure.title('Успешное создание курьера')
    def test_sucsess_create_courier(self):
        body = generate_create_courier_body()
        with allure.step('Проверка создания курьера'):
            response = CreateCourierMethods.create_courier(body)
        with allure.step('Запрос возвращает правильный код ответа'):
            assert response.status_code == 201
        with allure.step('Успешный запрос возвращает {"ok":true}'):
            assert (response.json() == {"ok": True})

    @allure.title('Проверка ошибки при создании дубликата логина курьера')
    def test_create_courier_dublicate_show_error(self):
        with allure.step('Генерация данных и создание первого курьера'):
            body = generate_create_courier_body()
            response_first = CreateCourierMethods.create_courier(body)
            assert response_first.status_code == 201, f"Первый курьер не создан: {response_first.text}"

        with allure.step('Проверка создания двух одинаковых курьеров'):
            response_duplicate = CreateCourierMethods.create_courier(body)

        with allure.step('Проверка вывода ошибки при дублировании логина'):
            assert response_duplicate.status_code == 409
            assert response_duplicate.json()["message"] == "Этот логин уже используется"

    @allure.title('Проверка вывода ошибки без указания обязательных полей при создании курьера')
    def test_create_courier_missing_required_fields(self):
        required_fields = ['login', 'password']
        for field in required_fields:
            with allure.step(f'Генерация тела запроса без поля "{field}"'):
                body = generate_create_courier_body()
                body.pop(field)

            with allure.step(f'Отправка запроса без поля "{field}"'):
                response = CreateCourierMethods.create_courier(body)

            with allure.step(f'Проверка вывода ошибки обязательных к заполнению полей "{field}"'):
                assert response.status_code == 400, f"Ожидали 400, получили {response.status_code} при отсутствии {field}"
                assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

