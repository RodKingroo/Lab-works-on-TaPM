from Stereo import Stereo
from Command import Command

class StereoOnWithCDCommand(Command):
    def __init__(self, stereo):
        if isinstance(stereo, Stereo):
            self.stereo = stereo
        else:
            raise NotImplementedError
        
    def execute(self):
        self.stereo.on()
        self.stereo.setCD()
        self.stereo.setVolume(11)
        
    def undo(self):
        self.stereo.off()