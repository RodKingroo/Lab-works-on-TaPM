# Copyright (c) 2022 RodKingroo
from Command import *
from HouseDoor import *

# House Door Open Command
class HouseDoorOpenCommand(Command):
    def __init__ (self, houseDoor):
        if isinstance(houseDoor, HouseDoor):
            self.houseDoor = houseDoor
        else:
            raise NotImplementedError
        
    def execute(self):
        self.houseDoor.open()
        
    def undo(self):
        self.houseDoor.close()
  
# House Door Close Command
class HouseDoorCloseCommand(Command):
    def __init__ (self, houseDoor):
        if isinstance(houseDoor, HouseDoor):
            self.houseDoor = houseDoor
        else:
            raise NotImplementedError
        
    def execute(self):
        self.houseDoor.close()
        
    def undo(self):
        self.houseDoor.open()