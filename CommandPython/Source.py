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

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Application()
    application.show()

sys.exit(app.exec())


# Command pattern CLIENT
#if __name__ == "__main__":
#    # Command pattern INVOKER
#    remote = RemoteControl()
#    
#    # Command pattern RECEIVERS
#    bedRoomCeilingFan = CeilingFan()
#    bedRoomStereo = Stereo()
#    bedRoomLight = Light()
#    garageStreetLight = StreetLight()
#    garageDoor = GarageDoor()
#    
#    # Command pattern COMMANDS
#    bedRoomСeilingFanStageOne = CeilingFanCommand.CeilingFanStageOneCommand(bedRoomCeilingFan)
#    bedRoomСeilingFanStageTwo = CeilingFanCommand.CeilingFanStageTwoCommand(bedRoomCeilingFan)
#    bedRoomСeilingFanStageThree = CeilingFanCommand.CeilingFanStageThreeCommand(bedRoomCeilingFan)
#    bedRoomСeilingFanStageFour = CeilingFanCommand.CeilingFanStageFourCommand(bedRoomCeilingFan)
#    bedRoomСeilingFanStageFive = CeilingFanCommand.CeilingFanStageFiveCommand(bedRoomCeilingFan)
#    bedRoomСeilingFanOff = CeilingFanCommand.CeilingFanOffCommand(bedRoomCeilingFan)
#    
#    bedRoomStereoCASSETE = StereoCommand.StereoOnCassetteCommand(bedRoomStereo)
#    bedRoomStereoCD = StereoCommand.StereoOnCDCommand(bedRoomStereo)
#    bedRoomStereoDVD = StereoCommand.StereoOnDVDCommand(bedRoomStereo)
#    bedRoomStereoRADIO = StereoCommand.StereoOnRadioCommand(bedRoomStereo)
#    bedRoomStereoCLOUDMUSIC = StereoCommand.StereoOnCloudMusicCommand(bedRoomStereo)
#    bedRoomStereoOff = StereoCommand.StereoOffCommand(bedRoomStereo)
#    
#    bedRoomLightStageOne = LightCommand.LightOnStageOneCommand(bedRoomLight)
#    bedRoomLightStageTwo = LightCommand.LightOnStageTwoCommand(bedRoomLight)
#    bedRoomLightStageThree = LightCommand.LightOnStageThreeCommand(bedRoomLight)
#    bedRoomLightStageFour = LightCommand.LightOnStageFourCommand(bedRoomLight)
#    bedRoomLightStageFive = LightCommand.LightOnStageFiveCommand(bedRoomLight)
#    bedRoomLightOff = LightCommand.LightOffCommand(bedRoomLight)
#    
#    garageStreetLightStageOne = StreetLightCommand.LightOnStageOneCommand(garageStreetLight)
#    garageStreetLightStageTwo = StreetLightCommand.LightOnStageTwoCommand(garageStreetLight)
#    garageStreetLightStageThree = StreetLightCommand.LightOnStageThreeCommand(garageStreetLight)
#    garageStreetLightStageFour = StreetLightCommand.LightOnStageFourCommand(garageStreetLight)
#    garageStreetLightStageFive = StreetLightCommand.LightOnStageFiveCommand(garageStreetLight)
#    garageStreetLightOff = StreetLightCommand.LightOffCommand(garageStreetLight)
#    
#    garageDoorOpen = GarageDoorCommand.GarageDoorOpenCommand(garageDoor)
#    garageDoorClose = GarageDoorCommand.GarageDoorCloseCommand(garageDoor)
#    
#    # Setting command to invocer
#    remote.setCommand(1, bedRoomСeilingFanStageOne, bedRoomСeilingFanOff)
#    remote.setCommand(2, bedRoomСeilingFanStageTwo, bedRoomСeilingFanOff)
#    remote.setCommand(3, bedRoomСeilingFanStageThree, bedRoomСeilingFanOff)
#    remote.setCommand(4, bedRoomСeilingFanStageFour, bedRoomСeilingFanOff)
#    remote.setCommand(5, bedRoomСeilingFanStageFive, bedRoomСeilingFanOff)
#    
#    remote.setCommand(6, bedRoomStereoCASSETE, bedRoomStereoOff)
#    remote.setCommand(7, bedRoomStereoCD, bedRoomStereoOff)
#    remote.setCommand(8, bedRoomStereoDVD, bedRoomStereoOff)
#    remote.setCommand(9, bedRoomStereoRADIO, bedRoomStereoOff)
#    remote.setCommand(10, bedRoomStereoCLOUDMUSIC, bedRoomStereoOff)
#    
#    remote.setCommand(11, bedRoomLightStageOne, bedRoomLightOff)
#    remote.setCommand(12, bedRoomLightStageTwo, bedRoomLightOff)
#    remote.setCommand(13, bedRoomLightStageThree, bedRoomLightOff)
#    remote.setCommand(14, bedRoomLightStageFour, bedRoomLightOff)
#    remote.setCommand(15, bedRoomLightStageFive, bedRoomLightOff)
#    
#    remote.setCommand(16, garageStreetLightStageOne, garageStreetLightOff)
#    remote.setCommand(17, garageStreetLightStageTwo, garageStreetLightOff)
#    remote.setCommand(18, garageStreetLightStageThree, garageStreetLightOff)
#    remote.setCommand(19, garageStreetLightStageFour, garageStreetLightOff)
#    remote.setCommand(20, garageStreetLightStageFive, garageStreetLightOff)
#    
#    remote.setCommand(21, garageDoorOpen, garageDoorClose)
#    
#    # Execitomg commands
#    remote.onButtonPress(21)
#    remote.offButtonPress(21)
#    remote.undoButtonPress()
