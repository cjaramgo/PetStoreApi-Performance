import json

from locust import *

from payloads.user import *
from payloads.pet import *
from utils.constants import *


class PetStore(SequentialTaskSet):

    username = None
    password = None
    pet_id = None

    @task
    def test_create_user(self):
        name = "Create User"
        route = "/user"
        payload = post_user()
        with self.client.post(route, catch_response=True, name=name, json=payload) as response:
            res_json = json.loads(response.text)
            self.username = res_json['username']
            self.password = res_json['password']
            if response.status_code == OK_CODE and response.elapsed.total_seconds() < 10:
                response.success()
            else:
                response.failure(
                    f"The status code was {response.status_code}, and the response time was {response.elapsed.total_seconds()}s")

    @task
    def test_login_user(self):
        name = "Login User"
        route = "/user/login"
        params = login_params(self.username, self.password)
        with self.client.get(route, catch_response=True, name=name, params=params) as response:
            if response.status_code == OK_CODE and response.elapsed.total_seconds() < 10:
                response.success()
            else:
                response.failure(
                    f"The status code was {response.status_code}, and the response time was {response.elapsed.total_seconds()}s")

    @task
    def test_get_user(self):
        name = "Get User by username"
        route = "/user/{}"
        with self.client.get(route.format(self.username), catch_response=True, name=name) as response:
            if response.status_code == OK_CODE and response.elapsed.total_seconds() < 10:
                response.success()
            else:
                response.failure(
                    f"The status code was {response.status_code}, and the response time was {response.elapsed.total_seconds()}s")

    @task
    def test_delete_user(self):
        name = "Delete User"
        route = "/user/{}"
        with self.client.delete(route.format(self.username), catch_response=True, name=name) as response:
            if response.status_code == OK_CODE and response.elapsed.total_seconds() < 10:
                response.success()
            else:
                response.failure(
                    f"The status code was {response.status_code}, and the response time was {response.elapsed.total_seconds()}s")

    @task
    def test_create_pet(self):
        name = "Create Pet"
        route = "/pet"
        payload = post_pet()
        with self.client.post(route, catch_response=True, name=name, json=payload) as response:
            res_json = json.loads(response.text)
            self.pet_id = res_json['id']
            if response.status_code == OK_CODE and response.elapsed.total_seconds() < 10:
                response.success()
            else:
                response.failure(
                    f"The status code was {response.status_code}, and the response time was {response.elapsed.total_seconds()}s")

    @task
    def test_get_pet(self):
        name = "Get Pet by ID"
        route = "/pet/{}"
        with self.client.get(route.format(self.pet_id), catch_response=True, name=name) as response:
            if response.status_code == OK_CODE and response.elapsed.total_seconds() < 10:
                response.success()
            else:
                response.failure(
                    f"The status code was {response.status_code}, and the response time was {response.elapsed.total_seconds()}s")

    @task
    def test_get_pets_by_status(self):
        name = "Get Pets by status"
        route = "/pet/findByStatus"
        params = pet_status()
        with self.client.get(route.format(self.username), catch_response=True, name=name, params=params) as response:
            if response.status_code == OK_CODE and response.elapsed.total_seconds() < 10:
                response.success()
            else:
                response.failure(
                    f"The status code was {response.status_code}, and the response time was {response.elapsed.total_seconds()}s")

    @task
    def test_get_pets_by_tags(self):
        name = "Get Pets by tags"
        route = "/pet/findByTags"
        params = pet_tags()
        with self.client.get(route.format(self.username), catch_response=True, name=name, params=params) as response:
            if response.status_code == OK_CODE and response.elapsed.total_seconds() < 10:
                response.success()
            else:
                response.failure(
                    f"The status code was {response.status_code}, and the response time was {response.elapsed.total_seconds()}s")

    @task
    def test_delete_pet(self):
        name = "Delete Pet"
        route = "/pet/{}"
        with self.client.delete(route.format(self.pet_id), catch_response=True, name=name) as response:
            if response.status_code == OK_CODE and response.elapsed.total_seconds() < 10:
                response.success()
            else:
                response.failure(
                    f"The status code was {response.status_code}, and the response time was {response.elapsed.total_seconds()}s")