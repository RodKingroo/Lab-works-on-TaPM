# Copyright (c) 2022 RodKingroo

from enums_class import *
from NYPizzaStore import NYPizzaStore
from ChicagoPizzaStore import ChicagoPizzaStore

if __name__ == "__main__":
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()

    pizza = chicagoStore.orderPizza(PizzaEnum.cheese)
    if pizza:
        print("Your pizza ", pizza.name)
    else:
        print("We are so sorry")
    print()
    

