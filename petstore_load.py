from locust import *
from petstore_tasks import PetStore


class PetStoreLoad(HttpUser):
    host = "http://localhost:8080/api/v3"
    tasks = [PetStore]
    wait_time = constant(2)
