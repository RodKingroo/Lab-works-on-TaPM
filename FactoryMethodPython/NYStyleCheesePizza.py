# Copyright (c) 2022 RodKingroo

from Pizza import Pizza
from enums_class import *

class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = NYPizzaName.Cheese
        self.dough = Dough.Thin
        self.sauce = Sauce.Marinara
        self.degree = Degree.Strong_Fire
        self.time = Time.Very_Fast
        self.toppings.extend((Ingredients.Reggiano, Ingredients.Mozarella, Ingredients.Reggiano))

    def box(self):
        print("Wrap in plastic wrap")



