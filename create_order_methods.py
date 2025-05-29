import requests

from data import Url


class CreateOrderMethods:
    @staticmethod
    def create_order(body):
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_ORDER_URL}', json=body)
        return response

