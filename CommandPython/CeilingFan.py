# Copyright (c) 2022 RodKingroo

class CeilingFan:
    def __init__(self):
        self.OFF = 0
        self.HIGH = 3
        self.speed = self.OFF
    
    def high(self):
        self.speed = self.HIGH
        print('Ceiling Fan Speed', self.speed)
        
    def off(self):
        self.speed = self.OFF
        print('Ceiling Fan Speed', self.speed)
    
    def getState(self):
        return self.speed