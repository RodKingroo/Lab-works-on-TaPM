# Copyright (c) 2022 RodKingroo
import sys
from StreetLight import *
from RemoteControl import *
from CeilingFan import *
from Stereo import *
from Light import *
from GarageDoor import *
from HouseDoor import *
import CeilingFanCommand, StereoCommand, LightCommand 
import StreetLightCommand, GarageDoorCommand, HouseDoorCommand

from PyQt5 import QtWidgets
from design import Ui_MainWindow

class Application(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ButtonInit()
        self.boolstate = True
        
    def ButtonInit(self):
        self.ui.ButtonOnCFHRSpeed1.clicked.connect(lambda: self.BackAndForth(1))
        self.ui.ButtonOnCFHRSpeed2.clicked.connect(lambda: self.BackAndForth(2))
        self.ui.ButtonOnCFHRSpeed3.clicked.connect(lambda: self.BackAndForth(3))
        self.ui.ButtonOnCFHRSpeed4.clicked.connect(lambda: self.BackAndForth(4))
        self.ui.ButtonOnCFHRSpeed5.clicked.connect(lambda: self.BackAndForth(5))
        
        self.ui.ButtonOnCFBRSpeed1.clicked.connect(lambda: self.BackAndForth(1))
        self.ui.ButtonOnCFBRSpeed2.clicked.connect(lambda: self.BackAndForth(2))
        self.ui.ButtonOnCFBRSpeed3.clicked.connect(lambda: self.BackAndForth(3))
        self.ui.ButtonOnCFBRSpeed4.clicked.connect(lambda: self.BackAndForth(4))
        self.ui.ButtonOnCFBRSpeed5.clicked.connect(lambda: self.BackAndForth(5))
        
        
        self.ui.ButtonOnSHRCassete.clicked.connect(lambda: self.BackAndForth(6))
        self.ui.ButtonOnSHRCD.clicked.connect(lambda: self.BackAndForth(7))
        self.ui.ButtonOnSHRDVD.clicked.connect(lambda: self.BackAndForth(8))
        self.ui.ButtonOnSHRRadio.clicked.connect(lambda: self.BackAndForth(9))
        self.ui.ButtonOnSHRCloud.clicked.connect(lambda: self.BackAndForth(10))
        
        self.ui.ButtonOnSBRCassete.clicked.connect(lambda: self.BackAndForth(6))
        self.ui.ButtonOnSBRCD.clicked.connect(lambda: self.BackAndForth(7))
        self.ui.ButtonOnSBRDVD.clicked.connect(lambda: self.BackAndForth(8))
        self.ui.ButtonOnSBRRadio.clicked.connect(lambda: self.BackAndForth(9))
        self.ui.ButtonOnSBRCloud.clicked.connect(lambda: self.BackAndForth(10))
        
        self.ui.ButtonOnLHRBright1.clicked.connect(lambda: self.BackAndForth(11))
        self.ui.ButtonOnLHRBright2.clicked.connect(lambda: self.BackAndForth(12))
        self.ui.ButtonOnLHRBright3.clicked.connect(lambda: self.BackAndForth(13))
        self.ui.ButtonOnLHRBright4.clicked.connect(lambda: self.BackAndForth(14))
        self.ui.ButtonOnLHRBright5.clicked.connect(lambda: self.BackAndForth(15))
        
        self.ui.ButtonOnLBRBright1.clicked.connect(lambda: self.BackAndForth(11))
        self.ui.ButtonOnLBRBright2.clicked.connect(lambda: self.BackAndForth(12))
        self.ui.ButtonOnLBRBright3.clicked.connect(lambda: self.BackAndForth(13))
        self.ui.ButtonOnLBRBright4.clicked.connect(lambda: self.BackAndForth(14))
        self.ui.ButtonOnLBRBright5.clicked.connect(lambda: self.BackAndForth(15))
        
        
        self.ui.ButtonOnSLHRBright1.clicked.connect(lambda: self.BackAndForth(16))
        self.ui.ButtonOnSLHRBright2.clicked.connect(lambda: self.BackAndForth(17))
        self.ui.ButtonOnSLHRBright3.clicked.connect(lambda: self.BackAndForth(18))
        self.ui.ButtonOnSLHRBright4.clicked.connect(lambda: self.BackAndForth(19))
        self.ui.ButtonOnSLHRBright5.clicked.connect(lambda: self.BackAndForth(20))
        
        self.ui.ButtonOnSLBRBright1.clicked.connect(lambda: self.BackAndForth(16))
        self.ui.ButtonOnSLBRBright2.clicked.connect(lambda: self.BackAndForth(17))
        self.ui.ButtonOnSLBRBright3.clicked.connect(lambda: self.BackAndForth(18))
        self.ui.ButtonOnSLBRBright4.clicked.connect(lambda: self.BackAndForth(19))
        self.ui.ButtonOnSLBRBright5.clicked.connect(lambda: self.BackAndForth(20))
        
        self.ui.ButtonOnGD.clicked.connect(lambda: self.BackAndForth(21))
        self.ui.ButtonOnHD.clicked.connect(lambda: self.BackAndForth(22))
        
        self.ui.ButtonUndo.clicked.connect(lambda: remote.undoButtonPress())
        
    def set_text_output(self, text):
        self.ui.Output.append(text)
        
    def BackAndForth(self, value):
        if self.boolstate == True:
            remote.onButtonPress(value)
            self.boolstate = False
        elif self.boolstate == False:
            remote.offButtonPress(value)
            self.boolstate = True

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Application()
    application.show()
    
    # Command pattern INVOKER
    remote = RemoteControl()
    # Command pattern RECEIVER
    ceilingFan = CeilingFan(application)
    stereo = Stereo(application)
    light = Light(application)
    streetLight = StreetLight(application)
    garageDoor = GarageDoor(application)
    houseDoor = HouseDoor(application)
    
    # Command pattern COMMANDS
    ceilingFanStageOne = CeilingFanCommand.CeilingFanStageOneCommand(ceilingFan)
    ceilingFanStageTwo = CeilingFanCommand.CeilingFanStageTwoCommand(ceilingFan)
    ceilingFanStageThree = CeilingFanCommand.CeilingFanStageThreeCommand(ceilingFan)
    ceilingFanStageFour = CeilingFanCommand.CeilingFanStageFourCommand(ceilingFan)
    ceilingFanStageFive = CeilingFanCommand.CeilingFanStageFiveCommand(ceilingFan)
    ceilingFanOff = CeilingFanCommand.CeilingFanOffCommand(ceilingFan)
    
    StereoCASSETE = StereoCommand.StereoOnCassetteCommand(stereo)
    StereoCD = StereoCommand.StereoOnCDCommand(stereo)
    StereoDVD = StereoCommand.StereoOnDVDCommand(stereo)
    StereoRADIO = StereoCommand.StereoOnRadioCommand(stereo)
    StereoCLOUDMUSIC = StereoCommand.StereoOnCloudMusicCommand(stereo)
    StereoOff = StereoCommand.StereoOffCommand(stereo)
    
    LightStageOne = LightCommand.LightOnStageOneCommand(light)
    LightStageTwo = LightCommand.LightOnStageTwoCommand(light)
    LightStageThree = LightCommand.LightOnStageThreeCommand(light)
    LightStageFour = LightCommand.LightOnStageFourCommand(light)
    LightStageFive = LightCommand.LightOnStageFiveCommand(light)
    LightOff = LightCommand.LightOffCommand(light)
    
    GarageDoorOpen = GarageDoorCommand.GarageDoorOpenCommand(garageDoor)
    GarageDoorClose = GarageDoorCommand.GarageDoorCloseCommand(garageDoor)
    
    HouseDoorOpen = HouseDoorCommand.HouseDoorOpenCommand(houseDoor)
    HouseDoorClose = HouseDoorCommand.HouseDoorCloseCommand(houseDoor)
    
    StreetLightStageOne = StreetLightCommand.LightOnStageOneCommand(streetLight)
    StreetLightStageTwo = StreetLightCommand.LightOnStageTwoCommand(streetLight)
    StreetLightStageThree = StreetLightCommand.LightOnStageThreeCommand(streetLight)
    StreetLightStageFour = StreetLightCommand.LightOnStageFourCommand(streetLight)
    StreetLightStageFive = StreetLightCommand.LightOnStageFiveCommand(streetLight)
    StreetLightOff = StreetLightCommand.LightOffCommand(streetLight)
    
    # Setting command to invocer
    remote.setCommand(1, ceilingFanStageOne, ceilingFanOff)
    remote.setCommand(2, ceilingFanStageTwo, ceilingFanOff)
    remote.setCommand(3, ceilingFanStageThree, ceilingFanOff)
    remote.setCommand(4, ceilingFanStageFour, ceilingFanOff)
    remote.setCommand(5, ceilingFanStageFive, ceilingFanOff)
    
    remote.setCommand(6, StereoCASSETE, StereoOff)
    remote.setCommand(7, StereoCD, StereoOff)
    remote.setCommand(8, StereoDVD, StereoOff)
    remote.setCommand(9, StereoRADIO, StereoOff)
    remote.setCommand(10, StereoCLOUDMUSIC, StereoOff)
    
    remote.setCommand(11, LightStageOne, LightOff)
    remote.setCommand(12, LightStageTwo, LightOff)
    remote.setCommand(13, LightStageThree, LightOff)
    remote.setCommand(14, LightStageFour, LightOff)
    remote.setCommand(15, LightStageFive, LightOff)
    
    remote.setCommand(16, StreetLightStageOne, StreetLightOff)
    remote.setCommand(17, StreetLightStageTwo, StreetLightOff)
    remote.setCommand(18, StreetLightStageThree, StreetLightOff)
    remote.setCommand(19, StreetLightStageFour, StreetLightOff)
    remote.setCommand(20, StreetLightStageFive, StreetLightOff)
    
    remote.setCommand(21, GarageDoorOpen, GarageDoorClose)
    remote.setCommand(22, HouseDoorOpen, HouseDoorClose)

sys.exit(app.exec())
