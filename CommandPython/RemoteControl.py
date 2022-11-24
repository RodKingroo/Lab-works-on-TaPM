# Copyright (c) 2022 RodKingroo

from Command import *
from NoCommand import *

class RemoteControl:
    def __init__(self):
        self.undoCommand = NoCommand()
        self.onCommands = []
        self.offCommands = []
        for i in range(47):
            self.onCommands.append(self.undoCommand)
            self.offCommands.append(self.undoCommand)
            
    def setCommand(self, slot, onCommand, offCommand):
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand
        
    def onButtonPress(self, slot):
        self.onCommands[slot].execute()
        self.undoCommand = self.onCommands[slot]
        
    def offButtonPress(self, slot):
        self.offCommands[slot].execute()
        self.undoCommand = self.offCommands[slot]
        
    def undoButtonPress(self):
        self.undoCommand.undo()