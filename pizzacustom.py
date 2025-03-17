#This file is for creating a custom pizza

"""
---BEcause you dont have it in the faker created data
#We will use this to ensure our requriement is satisfied

Our requirement is we need to use the kafka service to deploy the data
for the pizza orders given by the customers.
"""

import random
from faker.providers import BaseProvider

class pizzacustom(BaseProvider):
    pizzanames=['Ranch CHipotle','Memphis Barbeque','Delue Supreme',
                'Mediterrian',
                'WIsconsin 6-Cheese',
                'Neopoliation',
                'New York Style Flop',
                'Stuffed Chessy Garlic']

def pizza_name(self):
    return random.choice(self.pizzanames)