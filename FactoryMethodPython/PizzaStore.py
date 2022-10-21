# Copyright (c) 2022 RodKingroo

from abc import ABC, abstractmethod

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




