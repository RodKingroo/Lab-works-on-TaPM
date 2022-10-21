# Copyright (c) 2022 RodKingroo

from Pizza import Pizza 
from enums_class import *

class ChicagoStyleChorizoPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = NYPizzaName.Chorizo
        self.dough = Dough.Thick
        self.sauce = Sauce.Fat
        self.degree = Degree.Medium_Fire
        self.time = Time.Slow
        self.toppings.extend((Ingredients.Mozarella, Ingredients.Tomato, Ingredients.Chorizo))




