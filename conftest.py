import pytest

from create_courier_methods import CreateCourierMethods
from generators import generate_create_courier_body


@pytest.fixture
def generate_data_for_login():
    create_courier_body = generate_create_courier_body()
    login = create_courier_body["login"]
    password = create_courier_body["password"]
    yield [create_courier_body, login, password]
    courier_id = CreateCourierMethods.get_id_by_auth(login, password)
    CreateCourierMethods.delete_courier(courier_id)



