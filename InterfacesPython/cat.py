# Copyright (c) 2022 RodKingroo

from PyInt import IPet

class Cat(IPet):
    
    def setName(self, name):
    
        self.name = name

    def getName(self):

        return self.name

    def play(self):
        
        print(self.name, "любит играть с лазерной указкой")