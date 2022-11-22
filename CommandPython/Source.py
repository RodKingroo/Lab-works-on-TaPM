# Copyright (c) 2022 RodKingroo
from StreetLight import *
from RemoteControl import *
from CeilingFan import *
from Stereo import *
from Light import *
import CeilingFanCommand, StereoCommand, LightCommand, StreetLightCommand

# Command pattern CLIENT
if __name__ == "__main__":
    # Command pattern INVOKER
    remote = RemoteControl()
    
    # Command pattern RECEIVERS
    bedRoomCeilingFan = CeilingFan()
    bedRoomStereo = Stereo()
    bedRoomLight = Light()
    bedRoomStreetLight = StreetLight()
    
    # Command pattern COMMANDS
    bedRoomСeilingFanStageOne = CeilingFanCommand.CeilingFanStageOneCommand(bedRoomCeilingFan)
    bedRoomСeilingFanStageTwo = CeilingFanCommand.CeilingFanStageTwoCommand(bedRoomCeilingFan)
    bedRoomСeilingFanStageThree = CeilingFanCommand.CeilingFanStageThreeCommand(bedRoomCeilingFan)
    bedRoomСeilingFanStageFour = CeilingFanCommand.CeilingFanStageFourCommand(bedRoomCeilingFan)
    bedRoomСeilingFanStageFive = CeilingFanCommand.CeilingFanStageFiveCommand(bedRoomCeilingFan)
    bedRoomСeilingFanOff = CeilingFanCommand.CeilingFanOffCommand(bedRoomCeilingFan)
    
    bedRoomStereoCASSETE = StereoCommand.StereoOnCassetteCommand(bedRoomStereo)
    bedRoomStereoCD = StereoCommand.StereoOnCDCommand(bedRoomStereo)
    bedRoomStereoDVD = StereoCommand.StereoOnDVDCommand(bedRoomStereo)
    bedRoomStereoRADIO = StereoCommand.StereoOnRadioCommand(bedRoomStereo)
    bedRoomStereoCLOUDMUSIC = StereoCommand.StereoOnCloudMusicCommand(bedRoomStereo)
    bedRoomStereoOff = StereoCommand.StereoOffCommand(bedRoomStereo)
    
    bedRoomLightStageOne = LightCommand.LightOnStageOneCommand(bedRoomLight)
    bedRoomLightStageTwo = LightCommand.LightOnStageTwoCommand(bedRoomLight)
    bedRoomLightStageThree = LightCommand.LightOnStageThreeCommand(bedRoomLight)
    bedRoomLightStageFour = LightCommand.LightOnStageFourCommand(bedRoomLight)
    bedRoomLightStageFive = LightCommand.LightOnStageFiveCommand(bedRoomLight)
    bedRoomLightOff = LightCommand.LightOffCommand(bedRoomLight)
    
    bedRoomStreetLightStageOne = StreetLightCommand.LightOnStageOneCommand(bedRoomStreetLight)
    bedRoomStreetLightStageTwo = StreetLightCommand.LightOnStageTwoCommand(bedRoomStreetLight)
    bedRoomStreetLightStageThree = StreetLightCommand.LightOnStageThreeCommand(bedRoomStreetLight)
    bedRoomStreetLightStageFour = StreetLightCommand.LightOnStageFourCommand(bedRoomStreetLight)
    bedRoomStreetLightStageFive = StreetLightCommand.LightOnStageFiveCommand(bedRoomStreetLight)
    bedRoomStreetLightOff = StreetLightCommand.LightOffCommand(bedRoomStreetLight)
    
    # Setting command to invocer
    remote.setCommand(1, bedRoomСeilingFanStageOne, bedRoomСeilingFanOff)
    remote.setCommand(2, bedRoomСeilingFanStageTwo, bedRoomСeilingFanOff)
    remote.setCommand(3, bedRoomСeilingFanStageThree, bedRoomСeilingFanOff)
    remote.setCommand(4, bedRoomСeilingFanStageFour, bedRoomСeilingFanOff)
    remote.setCommand(5, bedRoomСeilingFanStageFive, bedRoomСeilingFanOff)
    
    remote.setCommand(6, bedRoomStereoCASSETE, bedRoomStereoOff)
    remote.setCommand(7, bedRoomStereoCD, bedRoomStereoOff)
    remote.setCommand(8, bedRoomStereoDVD, bedRoomStereoOff)
    remote.setCommand(9, bedRoomStereoRADIO, bedRoomStereoOff)
    remote.setCommand(10, bedRoomStereoCLOUDMUSIC, bedRoomStereoOff)
    
    remote.setCommand(11, bedRoomLightStageOne, bedRoomLightOff)
    remote.setCommand(12, bedRoomLightStageTwo, bedRoomLightOff)
    remote.setCommand(13, bedRoomLightStageThree, bedRoomLightOff)
    remote.setCommand(14, bedRoomLightStageFour, bedRoomLightOff)
    remote.setCommand(15, bedRoomLightStageFive, bedRoomLightOff)
    
    remote.setCommand(16, bedRoomStreetLightStageOne, bedRoomStreetLightOff)
    remote.setCommand(17, bedRoomStreetLightStageTwo, bedRoomStreetLightOff)
    remote.setCommand(18, bedRoomStreetLightStageThree, bedRoomStreetLightOff)
    remote.setCommand(19, bedRoomStreetLightStageFour, bedRoomStreetLightOff)
    remote.setCommand(20, bedRoomStreetLightStageFive, bedRoomStreetLightOff)
    
    
    # Execitomg commands
    remote.onButtonPress(20)
    remote.offButtonPress(20)
    remote.undoButtonPress()
