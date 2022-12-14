# Copyright (c) 2022 RodKingroo

from Pizza import Pizza 
from enums_class import *

class NYStyleCarbonaraPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = NYPizzaName.Carbonara
        self.dough = Dough.Thick
        self.sauce = Sauce.Alfredo
        self.degree = Degree.Medium_Fire
        self.time = Time.Slow
        self.toppings.extend((Ingredients.Cheder, Ingredients.Parmezan, Ingredients.Tomato, Ingredients.Mozarella))




