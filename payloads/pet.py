import random

from faker import Faker

fake = Faker()


def post_pet():
    categories = [{"id": 1, "name": 'Dogs'},
                  {"id": 2, "name": 'Cats'}]
    return {"id": random.randint(10, 1000),
            "name": fake.name(),
            "category": random.choice(categories),
            "photoUrls": [fake.image_url()],
            "tags": [{'id': '1', 'name': 'myTag'}],
            "status": 'available'
            }


def pet_status():
    status = ['available', 'pending', 'sold']
    return {"status": random.choice(status)}


def pet_tags():
    tags = ['tag1', 'tag2', 'myTag']
    return {"tags": random.choice(tags)}
