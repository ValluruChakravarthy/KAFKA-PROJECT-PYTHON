from faker import Faker
from pizzacustom import pizzacustom
import random

fake=Faker()
fake.add_provider(pizzacustom)

def messagetype():
    message={
            'name' :fake.name(),
            'address':fake.address(),
            'Gender':fake.passport_gender(),
            'email':fake.free_email(),
            'pizza':random.choice(pizzacustom.pizzanames)
    }
    return message
