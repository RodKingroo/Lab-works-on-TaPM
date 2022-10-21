# Copyright (c) 2022 RodKingroo

from Pizza import Pizza 
from enums_class import *

class NYStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = NYPizzaName.Pepperoni
        self.dough = Dough.Thin
        self.sauce = Sauce.Tomato
        self.degree = Degree.Medium_Fire
        self.time = Time.Medium
        self.toppings.extend((Ingredients.Mozarella, Ingredients.Pepperoni))




