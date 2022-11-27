/* Copyright (c) 2022 RodKingroo */
#include "RemoteControl.h"

#include "CeilingFan.h"
#include "CeilingFanCommand.h"

#include "Light.h"
#include "LightCommand.h"

#include "Stereo.h"
#include "StereoCommand.h"

/* Command pattern CLIENT */
int main()
{
    /* Command pattern INVOKER */
    unique_ptr<RemoteControl> remote = make_unique<RemoteControl>();

    /* Command pattern RECEIVERS */
    shared_ptr<CeilingFan> _ceilingFan = make_shared<CeilingFan>();
    shared_ptr<Light> _light = make_shared<Light>();
    shared_ptr<Stereo> _stereo = make_shared<Stereo>();

    /* Command pattern COMMANDS */
    shared_ptr<CeilingFanOneStateCommand> _commandCeilingFanStateOne = make_shared<CeilingFanOneStateCommand>(_ceilingFan);
    shared_ptr<CeilingFanTwoStateCommand> _commandCeilingFanStateTwo = make_shared<CeilingFanTwoStateCommand>(_ceilingFan);
    shared_ptr<CeilingFanThreeStateCommand> _commandCeilingFanStateThree = make_shared<CeilingFanThreeStateCommand>(_ceilingFan);
    shared_ptr<CeilingFanFourStateCommand> _commandCeilingFanStateFour = make_shared<CeilingFanFourStateCommand>(_ceilingFan);
    shared_ptr<CeilingFanFiveStateCommand> _commandCeilingFanStateFive = make_shared<CeilingFanFiveStateCommand>(_ceilingFan);
    shared_ptr<CeilingFanOffCommand> _commandCeilingFanOff = make_shared<CeilingFanOffCommand>(_ceilingFan);

    shared_ptr<LightOnStateOneCommand> _commandLightStateOne = make_shared<LightOnStateOneCommand>(_light);
    shared_ptr<LightOnStateTwoCommand> _commandLightStateTwo = make_shared<LightOnStateTwoCommand>(_light);
    shared_ptr<LightOnStateThreeCommand> _commandLightStateThree = make_shared<LightOnStateThreeCommand>(_light);
    shared_ptr<LightOnStateFourCommand> _commandLightStateFour = make_shared<LightOnStateFourCommand>(_light);
    shared_ptr<LightOnStateFiveCommand> _commandLightStateFive = make_shared<LightOnStateFiveCommand>(_light);
    shared_ptr<LightOffCommand> _commandLightOff = make_shared<LightOffCommand>(_light);

    shared_ptr<StereoOnCassetteCommand> _commandStereoOnCassette = make_shared<StereoOnCassetteCommand>(_stereo);
    shared_ptr<StereoOnCDCommand> _commandStereoOnCD = make_shared<StereoOnCDCommand>(_stereo);
    shared_ptr<StereoOnDVDCommand> _commandStereoOnDVD = make_shared<StereoOnDVDCommand>(_stereo);
    shared_ptr<StereoOnRadioCommand> _commandStereoOnRadio = make_shared<StereoOnRadioCommand>(_stereo);
    shared_ptr<StereoOnCloudCommand> _commandStereoOnCloud = make_shared<StereoOnCloudCommand>(_stereo);
    shared_ptr<StereoOffCommand> _commandStereoOff = make_shared<StereoOffCommand>(_stereo);

    /* Setting command to invocer */
    remote->setCommand(1, _commandCeilingFanStateOne, _commandCeilingFanOff);
    remote->setCommand(2, _commandCeilingFanStateTwo, _commandCeilingFanOff);
    remote->setCommand(3, _commandCeilingFanStateThree, _commandCeilingFanOff);
    remote->setCommand(4, _commandCeilingFanStateFour, _commandCeilingFanOff);
    remote->setCommand(5, _commandCeilingFanStateFive, _commandCeilingFanOff);

    remote->setCommand(6, _commandLightStateOne, _commandLightOff);
    remote->setCommand(7, _commandLightStateTwo, _commandLightOff);
    remote->setCommand(8, _commandLightStateThree, _commandLightOff);
    remote->setCommand(9, _commandLightStateFour, _commandLightOff);
    remote->setCommand(10, _commandLightStateFive, _commandLightOff);

    remote->setCommand(11, _commandStereoOnCassette, _commandStereoOff);
    remote->setCommand(12, _commandStereoOnCD, _commandStereoOff);
    remote->setCommand(13, _commandStereoOnDVD, _commandStereoOff);
    remote->setCommand(14, _commandStereoOnRadio, _commandStereoOff);
    remote->setCommand(15, _commandStereoOnCloud, _commandStereoOff);

    /* Execitomg commands */
    remote->onButtonPress(15);
    remote->offButtonPress(15);
    remote->undoButtonPress();

}