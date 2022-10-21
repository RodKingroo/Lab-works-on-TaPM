# Copyright (c) 2022 RodKingroo

from Pizza import Pizza 
from enums_class import *

class NYStyleViggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = NYPizzaName.Viggie
        self.dough = Dough.Thick
        self.sauce = Sauce.NoneSauce
        self.degree = Degree.Medium_Fire
        self.time = Time.Very_Slow
        self.toppings.extend((Ingredients.Parmezan, Ingredients.Tomato, Ingredients.Egg, Ingredients.Red, Ingredients.Spinate))

    def box(self):
        print("Wrap in foil")



