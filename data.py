class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER_URL = '/api/v1/courier'
    LOGIN_TO_SISTEM = '/api/v1/courier/login'
    LIST_OF_ORDERS_URL = '/api/v1/orders'
    CREATE_ORDER_URL = '/api/v1/orders'

class DataForCreateCourier:
    CREATE_LOGIN_BODY = {
        "login": "ninja",
        "password": "1234",
        "firstName": "saske"
    }

class DataForAuth:
    LOGIN_TO_SISTEM_BODY = {
        "login": "ninja",
        "password": "1234"
    }

class DataForOrderCreation:
    CREATE_ORDER_BODY = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
    }
