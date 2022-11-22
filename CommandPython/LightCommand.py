# Copyright (c) 2022 RodKingroo

from Light import *
from Command import *

def setUndo(light, prevBright):
    if prevBright == light.STAGE_ONE:
        light.stage_1()
    elif prevBright == light.STAGE_TWO:
        light.stage_2()
    elif prevBright == light.STAGE_THREE:
        light.stage_3()
    elif prevBright == light.STAGE_FOUR:
        light.stage_4()
    elif prevBright == light.STAGE_FIVE:
        light.stage_5()
        
    
# Light on Stage One command
class LightOnStageOneCommand(Command):
    def __init__(self, light):
        if isinstance(light, Light):
            self.light = light
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevBright = self.light.getState()
        self.light.on()
        self.light.stage_1()
        
    def undo(self):
        self.light.off()
        self.light = setUndo(self.light, self.prevBright)
        

# Light on Stage Two command
class LightOnStageTwoCommand(Command):
    def __init__(self, light):
        if isinstance(light, Light):
            self.light = light
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevBright = self.light.getState()
        self.light.on()
        self.light.stage_2()
        
    def undo(self):
        self.light.off()
        self.light = setUndo(self.light, self.prevBright)
        
# Light on Stage Three command
class LightOnStageThreeCommand(Command):
    def __init__(self, light):
        if isinstance(light, Light):
            self.light = light
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevBright = self.light.getState()
        self.light.on()
        self.light.stage_3()
        
    def undo(self):
        self.light.off()
        self.light = setUndo(self.light, self.prevBright)
        
# Light on Stage Four command
class LightOnStageFourCommand(Command):
    def __init__(self, light):
        if isinstance(light, Light):
            self.light = light
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevBright = self.light.getState()
        self.light.on()
        self.light.stage_4()
        
    def undo(self):
        self.light.off()
        self.light = setUndo(self.light, self.prevBright)
        
# Light on Stage Five command
class LightOnStageFiveCommand(Command):
    def __init__(self, light):
        if isinstance(light, Light):
            self.light = light
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevBright = self.light.getState()
        self.light.on()
        self.light.stage_5()
        
    def undo(self):
        self.light.off()
        self.light = setUndo(self.light, self.prevBright)
        
# Light Off command
class LightOffCommand(Command):
    def __init__(self, light):
        if isinstance(light, Light):
            self.light = light
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevBright = self.light.getState()
        self.light.off()
        
    def undo(self):
        self.light.on()
        self.light = setUndo(self.light, self.prevBright)
        
