# Copyright (c) 2022 RodKingroo

from CeilingFan import *
from Command import *

def setUndo(ceilingFan, prevSpeed):
    if prevSpeed == ceilingFan.OFF:
        ceilingFan.off()
    elif prevSpeed == ceilingFan.STAGE_ONE:
        ceilingFan.stage_1()
    elif prevSpeed == ceilingFan.STAGE_TWO:
        ceilingFan.stage_2()
    elif prevSpeed == ceilingFan.STAGE_THREE:
        ceilingFan.stage_3()
    elif prevSpeed == ceilingFan.STAGE_FOUR:
        ceilingFan.stage_4()
    elif prevSpeed == ceilingFan.STAGE_FIVE:
        ceilingFan.stage_5()
    return ceilingFan

# Ceiling Fan Off Command
class CeilingFanOffCommand(Command):
    def __init__(self, ceilingFan):
        if isinstance(ceilingFan, CeilingFan):
            self.ceilingFan = ceilingFan
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevSpeed = self.ceilingFan.getState()
        self.ceilingFan.off()
        
    def undo(self):
        self.ceilingFan.on()
        self.ceilingFan = setUndo(self.ceilingFan, self.prevSpeed)

# Ceiling Fan Stage One Command
class CeilingFanStageOneCommand(Command):
    def __init__(self, ceilingFan):
        if isinstance(ceilingFan, CeilingFan):
            self.ceilingFan = ceilingFan
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevSpeed = self.ceilingFan.getState()
        self.ceilingFan.on()
        self.ceilingFan.stage_1()
        
    def undo(self):
        self.ceilingFan.off()
        self.ceilingFan = setUndo(self.ceilingFan, self.prevSpeed)
        
        
# Ceiling Fan Stage Two Command
class CeilingFanStageTwoCommand(Command):
    def __init__(self, ceilingFan):
        if isinstance(ceilingFan, CeilingFan):
            self.ceilingFan = ceilingFan
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevSpeed = self.ceilingFan.getState()
        self.ceilingFan.on()
        self.ceilingFan.stage_2()    
        
    def undo(self):
        self.ceilingFan.off()
        self.ceilingFan = setUndo(self.ceilingFan, self.prevSpeed)
   
        
# Ceiling Fan Stage Three Command
class CeilingFanStageThreeCommand(Command):
    def __init__(self, ceilingFan):
        if isinstance(ceilingFan, CeilingFan):
            self.ceilingFan = ceilingFan
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevSpeed = self.ceilingFan.getState()
        self.ceilingFan.on()
        self.ceilingFan.stage_3()
        
    def undo(self):
        self.ceilingFan.off()
        self.ceilingFan = setUndo(self.ceilingFan, self.prevSpeed)
        
        
# Ceiling Fan Stage Four Command
class CeilingFanStageFourCommand(Command):
    def __init__(self, ceilingFan):
        if isinstance(ceilingFan, CeilingFan):
            self.ceilingFan = ceilingFan
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevSpeed = self.ceilingFan.getState()
        self.ceilingFan.on()
        self.ceilingFan.stage_4()
        
    def undo(self):
        self.ceilingFan.off()
        self.ceilingFan = setUndo(self.ceilingFan, self.prevSpeed)
        

# Ceiling Fan Stage Five Command
class CeilingFanStageFiveCommand(Command):
    def __init__(self, ceilingFan):
        if isinstance(ceilingFan, CeilingFan):
            self.ceilingFan = ceilingFan
        else:
            raise NotImplementedError
    
    def execute(self):
        self.prevSpeed = self.ceilingFan.getState()
        self.ceilingFan.on()
        self.ceilingFan.stage_5()
        
    def undo(self):
        self.ceilingFan.off()
        self.ceilingFan = setUndo(self.ceilingFan, self.prevSpeed)