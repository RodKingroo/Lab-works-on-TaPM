# Copyright (c) 2022 RodKingroo

class StreetLight:
    def __init__(self):
        self.OFF = 0
        self.STAGE_ONE = 20
        self.STAGE_TWO = 40
        self.STAGE_THREE = 60
        self.STAGE_FOUR = 80
        self.STAGE_FIVE = 100
        self.bright = self.OFF
    
    def on(self):
        print('Street Light on')
    
    def off(self):
        print('Street Light off')
        
    
    #setted Bright: Stage 1
    def stage_1(self):
        self.bright = self.STAGE_ONE
        print('Bright Street Light:', self.bright)
     
    #setted Bright: Stage 2   
    def stage_2(self):
        self.bright = self.STAGE_TWO
        print('Bright Street Light:', self.bright)
        
    #setted Bright: Stage 3   
    def stage_3(self):
        self.bright = self.STAGE_THREE
        print('Bright Street Light:', self.bright)
        
    #setted Bright: Stage 4   
    def stage_4(self):
        self.bright = self.STAGE_FOUR
        print('Bright Street Light:', self.bright)
        
    #setted Bright: Stage 5   
    def stage_5(self):
        self.bright = self.STAGE_FIVE
        print('Bright Street Light:', self.bright)
        
    def getState(self):
        return self.bright
        
    