# Copyright (c) 2022 RodKingroo

class HouseDoor:
    def __init__(self, ui):
        self.ui = ui
        
    
    def open(self):
        self.ui.set_text_output('Garage door open')
   
    def close(self):
        self.ui.set_text_output('Garage door close')
        
        
    
