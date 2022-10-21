# Copyright (c) 2022 RodKingroo

from Pizza import Pizza 
from enums_class import *

class NYStyleClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = NYPizzaName.Clam
        self.dough = Dough.Basic
        self.sauce = Sauce.Lemon
        self.degree = Degree.Low_Fire
        self.time = Time.Very_Slow
        self.toppings.extend((Ingredients.Parmezan, Ingredients.Clams, Ingredients.Romano, Ingredients.Red_Pepper))



