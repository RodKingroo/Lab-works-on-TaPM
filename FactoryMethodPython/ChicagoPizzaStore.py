# Copyright (c) 2022 RodKingroo

from enums_class import *
from PizzaStore import PizzaStore
from ChicagoStyleClamPizza import ChicagoStyleClamPizza
from ChicagoStyleCheesePizza import ChicagoStyleCheesePizza
from ChicagoStyleViggiePizza import ChicagoStyleViggiePizza
from ChicagoStyleChorizoPizza import ChicagoStyleChorizoPizza
from ChicagoStylePepperoniPizza import ChicagoStylePepperoniPizza
from ChicagoStyleCarbonaraPizza import ChicagoStyleCarbonaraPizza


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




