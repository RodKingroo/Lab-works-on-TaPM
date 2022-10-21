# Copyright (c) 2022 RodKingroo

from Pizza import Pizza 
from enums_class import *

class ChicagoStyleCarbonaraPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = NYPizzaName.Carbonara
        self.dough = Dough.Super_Thin
        self.sauce = Sauce.Alfredo
        self.degree = Degree.Medium_Fire
        self.time = Time.Fast
        self.toppings.extend((Ingredients.Cheder, Ingredients.Adyghe, Ingredients.Tomato, Ingredients.Red_Pepper))

    def box(self):
        print("Wrap in foil")

    def cut(self):
        print("Cut the pizza into triangular slices")




