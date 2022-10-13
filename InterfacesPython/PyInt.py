# Copyright (c) 2022 RodKingroo

from abc import ABC, abstractmethod

class IPet(ABC):
    
    @abstractmethod
    def setName(self,name):
    
        pass

    @abstractmethod
    def getName(self):
        
        pass

    @abstractmethod
    def play(self):
        
        pass

