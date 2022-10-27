# Copyright (c) 2022 RodKingroo

import sys, time
from PyQt5 import QtWidgets
from Design import Ui_MainWindow
from enums_class import *
from NYPizzaStore import NYPizzaStore
from ChicagoPizzaStore import ChicagoPizzaStore

class Application(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.i = 0
        self.styleAction()
        self.nameAction()

    def styleAction(self):
        self.ui.PizzaStyleEnum.addItem("", 0)
        self.ui.PizzaStyleEnum.addItem(ComboBoxStyleName.NewYork, StyleEnum.NewYork)
        self.ui.PizzaStyleEnum.addItem(ComboBoxStyleName.Chicago, StyleEnum.Chicago)

    def nameAction(self):
        self.ui.PizzaEnumCombo.addItem("", 0)
        self.ui.PizzaEnumCombo.addItem(ComboBoxPizzaName.cheese, PizzaEnum.cheese)
        self.ui.PizzaEnumCombo.addItem(ComboBoxPizzaName.pepperoni, PizzaEnum.pepperoni)
        self.ui.PizzaEnumCombo.addItem(ComboBoxPizzaName.carbonara, PizzaEnum.carbonara)
        self.ui.PizzaEnumCombo.addItem(ComboBoxPizzaName.chorizo, PizzaEnum.chorizo)
        self.ui.PizzaEnumCombo.addItem(ComboBoxPizzaName.clam, PizzaEnum.clam)
        self.ui.PizzaEnumCombo.addItem(ComboBoxPizzaName.viggie, PizzaEnum.viggie)
        self.ui.PizzaEnumCombo.activated.connect(self.selected)

    def selected(self):
        styleIndex = self.ui.PizzaStyleEnum.currentIndex()
        pizzaIndex = self.ui.PizzaEnumCombo.currentIndex()

        print("[", styleIndex, "] - [", pizzaIndex, "] ")

        if(styleIndex == StyleEnum.NewYork):
            Store = NYPizzaStore()
        elif(styleIndex == StyleEnum.Chicago):
            Store = ChicagoPizzaStore()
        else:
            pass

        pizza = Store.orderPizza(pizzaIndex)

        for i in range(101):
            time.sleep(0.1)
            if i == 20:
                self.ui.InfoCooking.setText(pizza.name + " is being prepared")
            elif i == 30:
                self.ui.InfoCooking.append(pizza.dough + " is made")
            elif i == 51:
                if(pizza.sauce != Sauce.NoneSauce):
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

