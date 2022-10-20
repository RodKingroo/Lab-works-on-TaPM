# Copyright (c) 2022 RodKingroo

from abc import ABC, abstractmethod
from enums_class import *

class Pizza:
    def __init__(self):
        self.toppings = []

    def prepare(self):
        print(self.name, "is being prepared")
        print(self.dough, "is made")
        if(self.sauce != SauceEnum.NoneSauce):
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
        print("Place pizza in official box")

class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = NYPizzaNameEnum.Cheese
        self.dough = DoughEnum.Thin
        self.sauce = SauceEnum.Marinara
        self.degree = DegreeEnum.Four_plusHalf_hundred
        self.time = TimeEnum.fast
        self.toppings.append(IngredientsEnum.Reggiano)

    def box(self):
        print("Wrap in plastic wrap")

class NYStylePepperoniCheese(Pizza):
    def __init__(self):
        super().__init__()
        

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = ChicagoPizzaNameEnum.Cheese
        self.dough = DoughEnum.Extra_Thick
        self.sauce = SauceEnum.Tomato
        self.degree = DegreeEnum.Five_hundred
        self.time = TimeEnum.fast
        self.toppings.append(IngredientsEnum.Mozarella)

    def cut(self):
        print("Cutting the pizza into square slices")

class PizzaStore(ABC):
    def orderPizza(self, pizzaType):
        pizza = self.createPizza(pizzaType)
        if pizza:
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.box()

        return pizza

    @abstractmethod
    def createPizza(self, pizzaType):
        pass

class NYPizzaStore(PizzaStore):
    def createPizza(self, pizzaType):
        if pizzaType == PizzaEnum.cheese:
            pizza = NYStyleCheesePizza()
            return pizza
        else:
            print("Have no this pizza type yet")
            return None

class ChicagoPizzaStore(PizzaStore):
    def createPizza(self, pizzaType):
        if pizzaType == PizzaEnum.cheese:
            pizza = ChicagoStyleCheesePizza()
            return pizza
        else:
            print("Have no this pizza type yet")
            return None

if __name__ == "__main__":
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()

    pizza = nyStore.orderPizza(PizzaEnum.cheese)
    if pizza:
        print("Your pizza ", pizza.name)
    else:
        print("We are so sorry")
    print()

    pizza = chicagoStore.orderPizza(PizzaEnum.cheese)
    if pizza:
        print("Your pizza ", pizza.name)
    else:
        print("We are so sorry")
    print()

    pizza = nyStore.orderPizza(PizzaEnum.pepperoni)
    if pizza:
        print("Your pizza ", pizza.name)
    else:
        print("We are so sorry")
    print()

