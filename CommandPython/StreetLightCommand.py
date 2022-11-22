# Copyright (c) 2022 RodKingroo

from StreetLight import *
from Command import *

def setUndo(streetLight, prevBright):
    if prevBright == streetLight.STAGE_ONE:
        streetLight.stage_1()
    elif prevBright == streetLight.STAGE_TWO:
        streetLight.stage_2()
    elif prevBright == streetLight.STAGE_THREE:
        streetLight.stage_3()
    elif prevBright == streetLight.STAGE_FOUR:
        streetLight.stage_4()
    elif prevBright == streetLight.STAGE_FIVE:
        streetLight.stage_5()
        
# Light on Stage One command
class LightOnStageOneCommand(Command):
    def __init__(self, streetLight):
        if isinstance(streetLight, StreetLight):
            self.streetLight = streetLight
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevBright = self.streetLight.getState()
        self.streetLight.on()
        self.streetLight.stage_1()
        
    def undo(self):
        self.streetLight.off()
        self.streetLight = setUndo(self.streetLight, self.prevBright)
        

# Light on Stage Two command
class LightOnStageTwoCommand(Command):
    def __init__(self, streetLight):
        if isinstance(streetLight, StreetLight):
            self.streetLight = streetLight
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevBright = self.streetLight.getState()
        self.streetLight.on()
        self.streetLight.stage_2()
        
    def undo(self):
        self.streetLight.off()
        self.streetLight = setUndo(self.streetLight, self.prevBright)
        
        
# Light on Stage Three command
class LightOnStageThreeCommand(Command):
    def __init__(self, streetLight):
        if isinstance(streetLight, StreetLight):
            self.streetLight = streetLight
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevBright = self.streetLight.getState()
        self.streetLight.on()
        self.streetLight.stage_3()
        
    def undo(self):
        self.streetLight.off()
        self.streetLight = setUndo(self.streetLight, self.prevBright)
        
        
        
# Light on Stage Four command
class LightOnStageFourCommand(Command):
    def __init__(self, streetLight):
        if isinstance(streetLight, StreetLight):
            self.streetLight = streetLight
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevBright = self.streetLight.getState()
        self.streetLight.on()
        self.streetLight.stage_4()
        
    def undo(self):
        self.streetLight.off()
        self.streetLight = setUndo(self.streetLight, self.prevBright)
        
        
# Light on Stage Five command
class LightOnStageFiveCommand(Command):
    def __init__(self, streetLight):
        if isinstance(streetLight, StreetLight):
            self.streetLight = streetLight
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevBright = self.streetLight.getState()
        self.streetLight.on()
        self.streetLight.stage_5()
        
    def undo(self):
        self.streetLight.off()
        self.streetLight = setUndo(self.streetLight, self.prevBright)
        
# Light Off command
class LightOffCommand(Command):
    def __init__(self, streetLight):
        if isinstance(streetLight, StreetLight):
            self.streetLight = streetLight
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevBright = self.streetLight.getState()
        self.streetLight.off()
        
    def undo(self):
        self.streetLight.on()
        self.streetLight = setUndo(self.streetLight, self.prevBright)
        
