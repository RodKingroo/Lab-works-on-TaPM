# Copyright (c) 2022 RodKingroo

import sys, unittest
from PyQt5 import QtWidgets
from Design import Ui_MainWindow
from Source import SimplePizzaFactory
from enums_class import *

class TestCase(unittest.TestCase):
    def test_createPizza(self):
        pizza = SimplePizzaFactory()
        pizza.createPizza(PizzaEnum.cheese)


if __name__ == '__main__':
	unittest.main()


