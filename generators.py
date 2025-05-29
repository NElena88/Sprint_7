from datetime import date, timedelta
import random
from turtle import color

from faker import Faker

fake = Faker()


def generate_create_courier_body():
    return {
        "login": fake.user_name(),
        "password": str(fake.random_int(min=1000, max=9999)),
        "firstName": fake.first_name()
    }

def generate_create_order_body():
    street = fake.street_name()
    order_body = {
    'firstName': fake.first_name(),
    'lastName': fake.last_name(),
    'address': f"Москва, {street}",
    'metroStation': random.randint(1, 30),
    'phone': '+79' + ''.join(random.choices('0123456789', k=9)),
    'rentTime': fake.random_int(min=1, max=30),
    'deliveryDate': (date.today() + timedelta(days=random.randint(1, 10))).isoformat()
    }
    if color is not None:
        order_body['color'] = color
    return order_body


