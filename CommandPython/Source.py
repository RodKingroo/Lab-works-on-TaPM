# Copyright (c) 2022 RodKingroo
from RemoteControl import *
from CeilingFan import *
from Stereo import *
import CeilingFanCommand, StereoCommand

# Command pattern CLIENT
if __name__ == "__main__":
    # Command pattern INVOKER
    remote = RemoteControl()
    
    # Command pattern RECEIVERS
    bedRoomCeilingFan = CeilingFan()
    bedRoomStereo = Stereo()
    
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
    
    
    # Execitomg commands
    remote.onButtonPress(10)
    remote.offButtonPress(10)
    remote.undoButtonPress()
