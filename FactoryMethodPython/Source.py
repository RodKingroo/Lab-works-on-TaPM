from abc import ABC, abstractmethod

class Pizza:
    def __init__(self):
        self.toppings = []

    def prepare(self):
        print("Preparing ", self.name)
        print("Tossing", self.dough)
        print("Adding", self.sauce)
        print("Adding toppings:")
        for topping in self.toppings:
            print("\t", topping)

    def bake(self):
        print("Bake for 25 min at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official box")

class NYCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin crust dough"
        self.sauce = "Marinara sauce"
        self.toppings.append("Grated Reggiano Cheese")

class ChicagoCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Sharaded Mozzarela Cheese")

    def cut(self):
        print("Cutting the pizza into square slices")

class PizzaStore(ABC):
    def orderPizza(self, pizzaType):
        pizza = self.createPizza(pizzaType)
        if pizza:
            pizza.prepare()
            pizza.bake()
            pizza.cut()

        return pizza

    @abstractmethod
    def createPizza(self, pizzaType):
        pass

class NYPizzaStore(PizzaStore):
    def createPizza(self, pizzaType):
        if pizzaType == "cheese":
            pizza = NYCheesePizza()
            return pizza
        else:
            print("Have no this pizza type yet")
            return None

class ChicagoPizzaStore(PizzaStore):
    def createPizza(self, pizzaType):
        if pizzaType == "cheese":
            pizza = ChicagoCheesePizza()
            return pizza
        else:
            print("Have no this pizza type yet")
            return None

if __name__ == "__main__":
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()

    pizza = nyStore.orderPizza("cheese")
    if pizza:
        print("Your pizza ", pizza.name)
    else:
        print("We are so sorry")
    print()

    pizza = chicagoStore.orderPizza("cheese")
    if pizza:
        print("Your pizza ", pizza.name)
    else:
        print("We are so sorry")
    print()

    pizza = nyStore.orderPizza("pepperony")
    if pizza:
        print("Your pizza ", pizza.name)
    else:
        print("We are so sorry")
    print()

