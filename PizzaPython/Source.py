# Copyright (c) 2022 RodKingroo

import sys, time
from PyQt5 import QtWidgets
from Design import Ui_MainWindow
from enums_class import *

class Pizza:
    def __init__(self):
        super().__init__()
        self.toppings = []

    def prepare(self):
        print(self.name, "is being prepared")
        print(self.dough, "is made")
        if(self.sauce != SauceEnum.NoneSauce):
            print(self.sauce, "is added")
        else:
            pass
        for topping in self.toppings:
            print("Adding", topping)

    def bake(self):
        print("Bake for", self.time, "at", self.degree)

    def cut(self):
        print("Cutting the pizza into diagonal slide")

    def box(self):
         print("Place pizza in official box")

class CheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = PizzaNameEnum.Cheese
        self.dough = DoughEnum.Basic
        self.sauce = SauceEnum.Fat
        self.time = TimeEnum.fast
        self.degree = DegreeEnum.Five_hundred
        self.toppings.append(IngredientsEnum.mozarella)
        self.toppings.append(IngredientsEnum.parmezan)
        self.toppings.append(IngredientsEnum.mozarella)

class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = PizzaNameEnum.Pepperoni
        self.dough = DoughEnum.Thin
        self.sauce = SauceEnum.Tomat
        self.time = TimeEnum.medium
        self.degree = DegreeEnum.Four_plusHalf_hundred
        self.toppings.append(IngredientsEnum.mozarella)
        self.toppings.append(IngredientsEnum.pepperoni)

class ChorizoPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = PizzaNameEnum.Chorizo
        self.dough = DoughEnum.Thin
        self.sauce = SauceEnum.Tomat
        self.time = TimeEnum.fast
        self.degree = DegreeEnum.Five_hundred
        self.toppings.append(IngredientsEnum.mozarella)
        self.toppings.append(IngredientsEnum.red)
        self.toppings.append(IngredientsEnum.chorizo)

class CarbanaraPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = PizzaNameEnum.Carbonara
        self.dough = DoughEnum.Basic
        self.sauce = SauceEnum.Alfredo
        self.time = TimeEnum.medium
        self.degree = DegreeEnum.Five_hundred
        self.toppings.append(IngredientsEnum.cheder)
        self.toppings.append(IngredientsEnum.parmezan)
        self.toppings.append(IngredientsEnum.tomato)
        self.toppings.append(IngredientsEnum.mozarella)

class ClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = PizzaNameEnum.Clam
        self.dough = DoughEnum.Basic
        self.sauce = SauceEnum.Lemon
        self.time = TimeEnum.slow
        self.degree = DegreeEnum.Four_plusHalf_hundred
        self.toppings.append(IngredientsEnum.parmezan)
        self.toppings.append(IngredientsEnum.clams)
        self.toppings.append(IngredientsEnum.romano)
        self.toppings.append(IngredientsEnum.red)

class ViggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = PizzaNameEnum.Viggie
        self.dough = DoughEnum.Basic
        self.sauce = SauceEnum.NoneSauce
        self.time = TimeEnum.very_slow
        self.degree = DegreeEnum.Three_Seventeen_five_Hunded
        self.toppings.append(IngredientsEnum.parmezan)
        self.toppings.append(IngredientsEnum.tomato)
        self.toppings.append(IngredientsEnum.egg)
        self.toppings.append(IngredientsEnum.red)
        self.toppings.append(IngredientsEnum.spinate)

class SimplePizzaFactory:
    def createPizza(self, pizzaType):
        if pizzaType == PizzaEnum.cheese:
            pizza = CheesePizza()
        elif pizzaType == PizzaEnum.pepperoni:
            pizza = PepperoniPizza()
        elif pizzaType == PizzaEnum.clam:
            pizza = ClamPizza()
        elif pizzaType == PizzaEnum.viggie:
            pizza = ViggiePizza()
        elif pizzaType == PizzaEnum.chorizo:
            pizza = ChorizoPizza()
        elif pizzaType == PizzaEnum.carbonara:
            pizza = CarbanaraPizza()
        return pizza

class PizzaStore:
    def __init__(self, pizzaFactory):
        self.factory = pizzaFactory
        

    def orderPizza(self, pizzaType):
        pizza = self.factory.createPizza(pizzaType)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        
        return pizza


class Application(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.i = 0
        self.comboAction();

    def comboAction(self):
        self.ui.PizzaEnumCombo.addItem(PizzaNameEnum.Cheese, PizzaEnum.cheese)
        self.ui.PizzaEnumCombo.addItem(PizzaNameEnum.Pepperoni, PizzaEnum.pepperoni)
        self.ui.PizzaEnumCombo.addItem(PizzaNameEnum.Clam, PizzaEnum.clam)
        self.ui.PizzaEnumCombo.addItem(PizzaNameEnum.Viggie, PizzaEnum.viggie)        
        self.ui.PizzaEnumCombo.addItem(PizzaNameEnum.Chorizo, PizzaEnum.chorizo)
        self.ui.PizzaEnumCombo.addItem(PizzaNameEnum.Carbonara, PizzaEnum.carbonara)
        self.ui.PizzaEnumCombo.activated.connect(self.selected)

    def selected(self, index):
        self.ui.YourPizza.setText(""); 
        pizzaFactory = SimplePizzaFactory()
        pizzaStore = PizzaStore(pizzaFactory)
        pizza = pizzaStore.orderPizza(self.ui.PizzaEnumCombo.itemData(index))

        for i in range(101):
            time.sleep(0.3)
            if i == 20:
                self.ui.InfoCooking.setText(pizza.name + " is being prepared")
            elif i == 30:
                self.ui.InfoCooking.append(pizza.dough + " is made")
            elif i == 50:
                if(pizza.sauce != SauceEnum.NoneSauce):
                    self.ui.InfoCooking.append(pizza.sauce + " is added")
                else:
                    pass
            elif i == 65:
                for topping in pizza.toppings:
                    self.ui.InfoCooking.append("Adding " + topping)
            elif i == 70:
                self.ui.InfoCooking.append("Bake for " + pizza.time + " at " + pizza.degree)
            elif i == 85:
                self.ui.InfoCooking.append("Cutting the pizza into diagonal slide")
            elif i == 98:
                self.ui.InfoCooking.append("Place pizza in official box")
            elif i == 100:
                self.ui.YourPizza.setText(pizza.name)

            self.ui.progressBar.setValue(i)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Application()
    application.show()

sys.exit(app.exec())