import random

from faker import Faker

fake = Faker()


def post_user():
    return {"id": random.randint(10, 1000),
               "username": fake.user_name(),
               "firstName": fake.first_name(),
               "lastName": fake.last_name(),
               "email": fake.email(),
               "password": fake.password(),
               "phone": fake.phone_number(),
               "userStatus": 1
               }


def login_params(user, password):
    return {"user_name": user, "password": password}
