# Copyright (c) 2022 RodKingroo

from Pizza import Pizza
from enums_class import *

class NYStyleChorizoPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = NYPizzaName.Chorizo
        self.dough = Dough.Basic
        self.sauce = Sauce.Tomato
        self.degree = Degree.Low_Fire
        self.time = Time.Very_Slow
        self.toppings.extend((Ingredients.Mozarella, Ingredients.Red_Pepper, Ingredients.Chorizo))




