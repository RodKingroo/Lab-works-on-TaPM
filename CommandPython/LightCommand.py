### Copyright (c) 2022 RodKingroo

from Light import Light
from Command import Command

class LightOnCommand(Command):
    def __init__(self, light):
        if isinstance(light, Light):
            self.light = light
        else:
            raise Exception('Invalid class Parameter')

        def execute (self):
            self.light.on()
        
        def undo(self):
            self.light.off()

class LightOffCommand(Command):
    def __init__(self, light):
        if isinstance(light, Light):
            self.light = light
        else:
            raise Exception("Invalid class Parameter") #timecode = 54:37

