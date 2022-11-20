# Copyright (c) 2022 RodKingroo

from CeilingFan import *
from Command import *

def setUndo(ceilingFan, prevSpeed):
    if prevSpeed == ceilingFan.HIGH:
        ceilingFan.high()
    elif prevSpeed == ceilingFan.OFF:
        ceilingFan.off()
    return ceilingFan

class CeilingFanHighCommand(Command):
    def __init__(self, ceilingFan):
        if isinstance(ceilingFan, CeilingFan):
            self.ceilingFan = ceilingFan
        else:
            raise NotImplementedError
    def execute(self):
        self.prevSpeed = self.ceilingFan.getState()
        self.ceilingFan.high()
    def undo(self):
        self.ceilingFan = setUndo(self.ceilingFan, self.prevSpeed)
        
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
        self.ceilingFan = setUndo(self.ceilingFan, self.prevSpeed)