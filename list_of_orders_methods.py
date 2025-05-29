import requests
from data import Url

class ListOfOrderMethods:
    @staticmethod
    def get_orders_list():
        response = requests.get(f"{Url.BASE_URL}{Url.CREATE_ORDER_URL}")
        return response
