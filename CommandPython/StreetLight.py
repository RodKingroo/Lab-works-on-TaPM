# Copyright (c) 2022 RodKingroo

class StreetLight:
    def __init__(self, ui):
        self.OFF = 0
        self.STAGE_ONE = 20
        self.STAGE_TWO = 40
        self.STAGE_THREE = 60
        self.STAGE_FOUR = 80
        self.STAGE_FIVE = 100
        self.bright = self.OFF
        self.ui = ui
    
    def on(self):
        self.ui.set_text_output('Street Light on')
    
    def off(self):
        self.ui.set_text_output('Street Light off')
        
    
    #setted Bright: Stage 1
    def stage_1(self):
        self.bright = self.STAGE_ONE
        self.ui.set_text_output('Bright Street Light:' + str(self.bright))
     
    #setted Bright: Stage 2   
    def stage_2(self):
        self.bright = self.STAGE_TWO
        self.ui.set_text_output('Bright Street Light:' + str(self.bright))
        
    #setted Bright: Stage 3   
    def stage_3(self):
        self.bright = self.STAGE_THREE
        self.ui.set_text_output('Bright Street Light:' + str(self.bright))
        
    #setted Bright: Stage 4   
    def stage_4(self):
        self.bright = self.STAGE_FOUR
        self.ui.set_text_output('Bright Street Light:' + str(self.bright))
        
    #setted Bright: Stage 5   
    def stage_5(self):
        self.bright = self.STAGE_FIVE
        self.ui.set_text_output('Bright Street Light:' + str(self.bright))
        
    def getState(self):
        return self.bright
        
    