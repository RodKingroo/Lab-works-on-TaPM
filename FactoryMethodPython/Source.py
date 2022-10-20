# Copyright (c) 2022 RodKingroo

from abc import ABC, abstractmethod
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

class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = NYPizzaName.Cheese
        self.dough = Dough.Thin
        self.sauce = Sauce.Marinara
        self.degree = Degree.Strong_Fire
        self.time = Time.Very_Fast
        self.toppings.extend((Ingredients.Reggiano, Ingredients.Mozarella, Ingredients.Reggiano))

    def box(self):
        print("Wrap in plastic wrap")

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

class NYStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = NYPizzaName.Pepperoni
        self.dough = Dough.Thin
        self.sauce = Sauce.Tomato
        self.degree = Degree.Medium_Fire
        self.time = Time.Medium
        self.toppings.extend((Ingredients.Mozarella, Ingredients.Pepperoni))

class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = ChicagoPizzaName.Pepperoni
        self.dough = Dough.Very_Thin
        self.sauce = Sauce.Tomato
        self.degree = Degree.Medium_Fire
        self.time = Time.Fast
        self.toppings.extend((Ingredients.Mozarella, Ingredients.Pepperoni, Ingredients.Cheder))


class NYStyleChorizoPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = NYPizzaName.Chorizo
        self.dough = Dough.Basic
        self.sauce = Sauce.Tomato
        self.degree = Degree.Low_Fire
        self.time = Time.Very_Slow
        self.toppings.extend((Ingredients.Mozarella, Ingredients.Red_Pepper, Ingredients.Chorizo))

class ChicagoStyleChorizoPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = NYPizzaName.Chorizo
        self.dough = Dough.Thick
        self.sauce = Sauce.Fat
        self.degree = Degree.Medium_Fire
        self.time = Time.Slow
        self.toppings.extend((Ingredients.Mozarella, Ingredients.Tomato, Ingredients.Chorizo))

class NYStyleCarbonaraPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = NYPizzaName.Carbonara
        self.dough = Dough.Thick
        self.sauce = Sauce.Alfredo
        self.degree = Degree.Medium_Fire
        self.time = Time.Slow
        self.toppings.extend((Ingredients.Cheder, Ingredients.Parmezan, Ingredients.Tomato, Ingredients.Mozarella))

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
        
class NYStyleClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = NYPizzaName.Clam
        self.dough = Dough.Basic
        self.sauce = Sauce.Lemon
        self.degree = Degree.Low_Fire
        self.time = Time.Very_Slow
        self.toppings.extend((Ingredients.Parmezan, Ingredients.Clams, Ingredients.Romano, Ingredients.Red_Pepper))

class ChicagoStyleClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = NYPizzaName.Clam
        self.dough = Dough.Basic
        self.sauce = Sauce.Lemon
        self.degree = Degree.Medium_Fire
        self.time = Time.Very_Slow
        self.toppings.extend((Ingredients.Parmezan, Ingredients.Clams, Ingredients.Cheder, Ingredients.Red_Pepper))

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

class NYStyleViggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = NYPizzaName.Viggie
        self.dough = Dough.Thick
        self.sauce = Sauce.NoneSauce
        self.degree = Degree.Strong_Fire
        self.time = Time.Medium
        self.toppings.extend((Ingredients.Parmezan, Ingredients.Tomato, Ingredients.Egg, Ingredients.Spinate))

class ChicagoStyleViggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = ChicagoPizzaName.Viggie
        self.dough = Dough.Extra_Thick
        self.sauce = Sauce.Milk
        self.degree = Degree.Medium_Fire
        self.time = Time.Medium
        self.toppings.extend((Ingredients.Parmezan, Ingredients.Tomato, Ingredients.Spinate))

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
        elif pizzaType == PizzaEnum.pepperoni:
            pizza = NYStylePepperoniPizza()
            return pizza
        elif pizzaType == PizzaEnum.clam:
            pizza = NYStyleClamPizza()
            return pizza
        elif pizzaType == PizzaEnum.viggie:
            pizza = NYStyleViggiePizza()
            return pizza
        elif pizzaType == PizzaEnum.chorizo:
            pizza = NYStyleChorizoPizza()
            return pizza
        elif pizzaType == PizzaEnum.carbonara:
            pizza = NYStyleCarbonaraPizza()
            return pizza
        else:
            print("Have no this pizza type yet")
            return None

class ChicagoPizzaStore(PizzaStore):
    def createPizza(self, pizzaType):
        if pizzaType == PizzaEnum.cheese:
            pizza = ChicagoStyleCheesePizza()
            return pizza
        elif pizzaType == PizzaEnum.pepperoni:
            pizza = ChicagoStylePepperoniPizza()
            return pizza
        elif pizzaType == PizzaEnum.clam:
            pizza = ChicagoStyleClamPizza()
            return pizza
        elif pizzaType == PizzaEnum.viggie:
            pizza = ChicagoStyleViggiePizza()
            return pizza
        elif pizzaType == PizzaEnum.chorizo:
            pizza = ChicagoStyleChorizoPizza()
            return pizza
        elif pizzaType == PizzaEnum.carbonara:
            pizza = ChicagoStyleCarbonaraPizza()
            return pizza
        else:
            print("Have no this pizza type yet")
            return None

if __name__ == "__main__":
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()

    pizza = nyStore.orderPizza(PizzaEnum.carbonara)
    if pizza:
        print("Your pizza ", pizza.name)
    else:
        print("We are so sorry")
    print()
    

