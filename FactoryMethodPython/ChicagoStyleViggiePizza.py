# Copyright (c) 2022 RodKingroo

from Pizza import Pizza 
from enums_class import *

class ChicagoStyleViggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = ChicagoPizzaName.Viggie
        self.dough = Dough.Extra_Thick
        self.sauce = Sauce.Milk
        self.degree = Degree.Medium_Fire
        self.time = Time.Medium
        self.toppings.extend((Ingredients.Parmezan, Ingredients.Tomato, Ingredients.Spinate))




