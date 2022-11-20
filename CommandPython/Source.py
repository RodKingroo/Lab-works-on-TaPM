# Copyright (c) 2022 RodKingroo
from RemoteControl import *
from CeilingFan import *
import CeilingFanCommand 

# Command pattern CLIENT
if __name__ == "__main__":
    # Command pattern INVOKER
    remote = RemoteControl()
    
    # Command pattern RECEIVERS
    bedRoomCeilingFan = CeilingFan()
    
    # Command pattern COMMANDS
    bedRoomСeilingFanHigh = CeilingFanCommand.CeilingFanHighCommand(bedRoomCeilingFan)
    bedRoomСeilingFanOff = CeilingFanCommand.CeilingFanOffCommand(bedRoomCeilingFan)
    
    # Setting command to invocer
    remote.setCommand(1, bedRoomСeilingFanHigh, bedRoomСeilingFanOff)
    
    # Execitomg commands
    remote.onButtonPress(1)
    remote.offButtonPress(1)
    remote.undoButtonPress()
