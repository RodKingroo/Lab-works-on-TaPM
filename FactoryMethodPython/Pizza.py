# Copyright (c) 2022 RodKingroo

from enums_class import *

class Pizza:
    def __init__(self):
        self.toppings = []

    def prepare(self):
        print(self.name, "is being prepared")
        print(self.dough, "is made")
        if(self.sauce != Sauce.NoneSauce):
            print(self.sauce, "is added")
        else:
            pass
        print("Adding toppings:")
        for topping in self.toppings:
            print("\t", topping)

    def bake(self):
        print("Bake for", self.degree, "at", self.time, "deegree")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Wrap in official box")




