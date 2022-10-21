# Copyright (c) 2022 RodKingroo

from Pizza import Pizza
from enums_class import *

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = ChicagoPizzaName.Cheese
        self.dough = Dough.Extra_Thick
        self.sauce = Sauce.Tomato
        self.degree = Degree.Medium_Fire
        self.time = Time.Medium
        self.toppings.extend((Ingredients.Mozarella, Ingredients.Adyghe, Ingredients.Reggiano))

    def cut(self):
        print("Cutting the pizza into square slices")




