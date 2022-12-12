import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza
from pizzas.models import Topping

pizza_test = Pizza.objects.all()
topping_test = Topping.objects.all()

print(pizza_test)
print(topping_test)

for p in pizza_test:
    print(p)
    print(p.pizza_name)


topping_entry_test = Topping.objects.filter(Pizza=p)

for g in topping_entry_test:
    print(g)
    print(g.pizza)
    print(g.topping_name)