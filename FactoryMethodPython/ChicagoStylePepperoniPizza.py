# Copyright (c) 2022 RodKingroo

from Pizza import Pizza
from enums_class import *

class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = ChicagoPizzaName.Pepperoni
        self.dough = Dough.Super_Thin
        self.sauce = Sauce.Tomato
        self.degree = Degree.Medium_Fire
        self.time = Time.Fast
        self.toppings.extend((Ingredients.Mozarella, Ingredients.Pepperoni, Ingredients.Cheder))



