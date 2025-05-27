import requests

from data import Url, DataForCreateCourier
from generators import generate_create_courier_body


class CreateCourierMethods:
    @staticmethod
    def create_courier(body):
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER_URL}', json=body)
        return response

    @staticmethod
    def login_courier(body):
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_TO_SISTEM}', json=body)
        return response

    @staticmethod
    def register_and_return_credentials():
        body = generate_create_courier_body()
        response = CreateCourierMethods.create_courier(body)
        if response.status_code == 201:
            return {"login": body["login"], "password": body["password"]}
        return None

    @staticmethod
    def get_id_by_auth(login, password):
        params = {'login':login, 'password':password}
        response = requests.get(f'{Url.BASE_URL}{Url.CREATE_COURIER_URL}', json=params)
        courier_id = response.json()
        return courier_id

    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f'{Url.BASE_URL}{Url.CREATE_COURIER_URL}/{courier_id}')




