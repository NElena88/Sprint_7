import allure

from create_courier_methods import CreateCourierMethods


class TestAuthCourier:
    @allure.title('Проверка успешной авторизации курьера')
    def test_sucsess_auth_courier_login(self):
        credentials = CreateCourierMethods.register_and_return_credentials()
        login_payload = {
            "login": credentials["login"],
            "password": credentials["password"]
        }
        response = CreateCourierMethods.login_courier(login_payload)
        assert response.status_code == 200
        with allure.step('Проверка возврата id при успешной авторизации'):
            assert "id" in response.json()

    @allure.title('Проверка авторизации курьера без заполнения одного из обязательных полей')
    def test_auth_missing_login_show_error(self):
        with allure.step('Проверка вывода ошибки при авторизации без логина'):
            credentials = CreateCourierMethods.register_and_return_credentials()
            payload = {"password": credentials["password"]}
            response = CreateCourierMethods.login_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Проверка авторизации курьера без заполнения одного из обязательных полей')
    def test_auth_missing_password_show_error(self):
        with allure.step('Проверка вывода ошибки при авторизации без пароля'):
            credentials = CreateCourierMethods.register_and_return_credentials()
            payload = {"login": credentials["login"]}
            response = CreateCourierMethods.login_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Проверка вывода ошибки при авторизации с неправильными логином или паролем')
    def test_courier_login_wrong_credentials(self):
        credentials = CreateCourierMethods.register_and_return_credentials()
        login_payload = {"login": credentials["login"], "password": "wrongpassword"}

        response = CreateCourierMethods.login_courier(login_payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title('Проверка вывода ошибки при авторизации несуществующего пользователя')
    def test_login_nonexistent_user(self):
        login_payload = {"login": "nonexistentuser123", "password": "anyPassword123"}
        response = CreateCourierMethods.login_courier(login_payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"


