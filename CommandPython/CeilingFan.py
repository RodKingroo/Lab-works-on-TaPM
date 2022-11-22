# Copyright (c) 2022 RodKingroo

class CeilingFan:
    def __init__(self):
        self.OFF = 0
        self.STAGE_ONE = 1
        self.STAGE_TWO = 2
        self.STAGE_THREE = 4
        self.STAGE_FOUR = 8
        self.STAGE_FIVE = 16
        self.speed = self.OFF
    
    def on(self):
        print('Ceiling Fan On')
    
    def off(self):
        print("Ceiling Fan Off")
    
    def stage_1(self):
        self.speed = self.STAGE_ONE
        print('Ceiling Fan Speed', self.speed)
        
    def stage_2(self):
        self.speed = self.STAGE_TWO
        print('Ceiling Fan Speed', self.speed)
    
    def stage_3(self):
        self.speed = self.STAGE_THREE
        print('Ceiling Fan Speed', self.speed)
        
    def stage_4(self):
        self.speed = self.STAGE_FOUR
        print('Ceiling Fan Speed', self.speed)
        
    def stage_5(self):
        self.speed = self.STAGE_FIVE
        print('Ceiling Fan Speed', self.speed)
    
    def getState(self):
        return self.speed