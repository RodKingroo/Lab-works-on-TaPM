# Copyright (c) 2022 RodKingroo

from Stereo import *
from Command import *

def setUndo(stereo, prevType):
    if prevType == stereo.CASSETTE:
        stereo.setCASSETTE()
        stereo.setVolume(10)
    elif prevType == stereo.CD:
        stereo.setCD()
        stereo.setVolume(5)
    elif prevType == stereo.DVD:
        stereo.setDVD()
        stereo.setVolume(15)
    elif prevType == stereo.RADIO:
        stereo.setRADIO()
        stereo.setVolume(50)
    elif prevType == stereo.CLOUDMUSIC:
        stereo.setCLOUDMUSIC()
        stereo.setVolume(70)
        
        
# Stereo on CASSETTE command
class StereoOnCassetteCommand(Command):
    def __init__(self, stereo):
        if isinstance(stereo, Stereo):
            self.stereo = stereo
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevType = self.stereo.getState()
        self.stereo.on()
        self.stereo.setCASSETTE()
        self.stereo.setVolume(10)
            
    def undo(self):
        self.stereo.off()
        self.stereo = setUndo(self.stereo, self.prevType)
        
        

# Stereo On CD Command
class StereoOnCDCommand(Command):
    def __init__(self, stereo):
        if isinstance(stereo, Stereo):
            self.stereo = stereo
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevType = self.stereo.getState()
        self.stereo.on()
        self.stereo.setCD()
        self.stereo.setVolume(5)
        
    def undo(self):
        self.stereo.off()
        self.stereo = setUndo(self.stereo, self.prevType)
        

# Stereo On DVD Command
class StereoOnDVDCommand(Command):
    def __init__(self, stereo):
        if isinstance(stereo, Stereo):
            self.stereo = stereo
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevType = self.stereo.getState()
        self.stereo.on()
        self.stereo.setDVD()
        self.stereo.setVolume(15)
        
    def undo(self):
        self.stereo.off()
        self.stereo = setUndo(self.stereo, self.prevType)
        
        
        
# Stereo On Radio Command
class StereoOnRadioCommand(Command):
    def __init__(self, stereo):
        if isinstance(stereo, Stereo):
            self.stereo = stereo
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevType = self.stereo.getState()
        self.stereo.on()
        self.stereo.setRADIO()
        self.stereo.setVolume(50)
        
    def undo(self):
        self.stereo.off()
        self.stereo = setUndo(self.stereo, self.prevType)
        
        
# Stereo on Cloud Music command
class StereoOnCloudMusicCommand(Command):
    def __init__(self, stereo):
        if isinstance(stereo, Stereo):
            self.stereo = stereo
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevType = self.stereo.getState()
        self.stereo.on()
        self.stereo.setCLOUDMUSIC()
        self.stereo.setVolume(70)
        
    def undo(self):
        self.stereo.off()
        self.stereo = setUndo(self.stereo, self.prevType)
        
               
#Stereo Off Command
class StereoOffCommand(Command):
    def __init__(self, stereo):
        if isinstance(stereo, Stereo):
            self.stereo = stereo
        else:
            raise NotImplementedError
        
    def execute(self):
        self.prevType = self.stereo.getState()
        self.stereo.off()
        
    def undo(self):
        self.stereo.on()
        self.stereo = setUndo(self.stereo, self.prevType)