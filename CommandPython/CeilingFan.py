# Copyright (c) 2022 RodKingroo
from design import Ui_MainWindow

class CeilingFan:
    def __init__(self, ui):
        self.OFF = 0
        self.STAGE_ONE = 1
        self.STAGE_TWO = 2
        self.STAGE_THREE = 4
        self.STAGE_FOUR = 8
        self.STAGE_FIVE = 16
        self.speed = self.OFF
        self.ui = ui
    
    def on(self):
        self.ui.set_text_output("Ceiling Fan on")
    
    def off(self):
        self.ui.set_text_output("Ceiling Fan off")
    
    def stage_1(self):
        self.speed = self.STAGE_ONE
        self.ui.set_text_output('Ceiling Fan Speed: ' + str(self.speed))
        
    def stage_2(self):
        self.speed = self.STAGE_TWO
        self.ui.set_text_output('Ceiling Fan Speed: ' + str(self.speed))
    
    def stage_3(self):
        self.speed = self.STAGE_THREE
        self.ui.set_text_output('Ceiling Fan Speed: ' + str(self.speed))
        
    def stage_4(self):
        self.speed = self.STAGE_FOUR
        self.ui.set_text_output('Ceiling Fan Speed: ' + str(self.speed))
        
    def stage_5(self):
        self.speed = self.STAGE_FIVE
        self.ui.set_text_output('Ceiling Fan Speed: ' + str(self.speed))
    
    def getState(self):
        return self.speed