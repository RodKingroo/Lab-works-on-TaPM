# Copyright (c) 2022 RodKingroo
from Command import *
from GarageDoor import *

# Garage Door Open Command
class GarageDoorOpenCommand(Command):
    def __init__ (self, garageDoor):
        if isinstance(garageDoor, GarageDoor):
            self.garageDoor = garageDoor
        else:
            raise NotImplementedError
        
    def execute(self):
        self.garageDoor.open()
        
    def undo(self):
        self.garageDoor.close()
  
# Garage Door Close Command      
class GarageDoorCloseCommand(Command):
    def __init__ (self, garageDoor):
        if isinstance(garageDoor, GarageDoor):
            self.garageDoor = garageDoor
        else:
            raise NotImplementedError
        
    def execute(self):
        self.garageDoor.close()
        
    def undo(self):
        self.garageDoor.open()