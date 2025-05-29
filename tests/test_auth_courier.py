import allure
from data import MessageText
from create_courier_methods import CreateCourierMethods


class TestAuthCourier:
    @allure.title('Проверка успешной авторизации курьера')
    def test_sucsess_auth_courier_login(self, generate_data_for_login):
        create_courier_body, login, password = generate_data_for_login
        login_payload = {
            "login": login,
            "password": password
        }
        response = CreateCourierMethods.login_courier(login_payload)
        assert response.status_code == 200
        with allure.step('Проверка возврата id при успешной авторизации'):
            assert "id" in response.json()

    @allure.title('Проверка авторизации курьера без заполнения одного из обязательных полей')
    def test_auth_missing_login_show_error(self, generate_data_for_login):
        with allure.step('Проверка вывода ошибки при авторизации без логина'):
            create_courier_body, login, password = generate_data_for_login
            payload = {"password": password}
            response = CreateCourierMethods.login_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == MessageText.MISSING_CREDENTIALS_MSG

    @allure.title('Проверка авторизации курьера без заполнения одного из обязательных полей')
    def test_auth_missing_password_show_error(self, generate_data_for_login):
        with allure.step('Проверка вывода статус-кода 400 при авторизации без пароля'):
            create_courier_body, login, password = generate_data_for_login
            payload = {"login": login}
            response = CreateCourierMethods.login_courier(payload)
            assert response.status_code == 400

        with allure.step('Проверка вывода ошибки при авторизации без пароля'):
            assert response.json()["message"] == MessageText.MISSING_CREDENTIALS_MSG

    @allure.title('Проверка вывода ошибки при авторизации с неправильными логином или паролем')
    def test_courier_login_wrong_credentials(self, generate_data_for_login):
        create_courier_body, login, password = generate_data_for_login
        login_payload = {"login": login, "password": "wrongpassword"}

        response = CreateCourierMethods.login_courier(login_payload)

        assert response.status_code == 404
        assert response.json()["message"] == MessageText.ACCOUNT_NOT_FOUND_MSG

    @allure.title('Проверка вывода ошибки при авторизации несуществующего пользователя')
    def test_login_nonexistent_user(self):
        login_payload = {"login": "nonexistentuser123", "password": "anyPassword123"}
        response = CreateCourierMethods.login_courier(login_payload)

        assert response.status_code == 404
        assert response.json()["message"] == MessageText.ACCOUNT_NOT_FOUND_MSG


