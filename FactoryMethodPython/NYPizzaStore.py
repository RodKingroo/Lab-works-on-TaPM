# Copyright (c) 2022 RodKingroo

from enums_class import *
from PizzaStore import PizzaStore
from NYStyleClamPizza import NYStyleClamPizza
from NYStyleCheesePizza import NYStyleCheesePizza
from NYStyleViggiePizza import NYStyleViggiePizza
from NYStyleChorizoPizza import NYStyleChorizoPizza
from NYStylePepperoniPizza import NYStylePepperoniPizza
from NYStyleCarbonaraPizza import NYStyleCarbonaraPizza


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




