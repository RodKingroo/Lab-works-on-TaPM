#include "RemoteControl.h"

#include "CeilingFan.h"
#include "CeilingFanCommand.h"

/* Command pattern CLIENT */
int main()
{
    /* Command pattern INVOKER */
    unique_ptr<RemoteControl> remote = make_unique<RemoteControl>();

    /* Command pattern RECEIVERS */
    shared_ptr<CeilingFan> _ceilingFan = make_shared<CeilingFan>();

    /* Command pattern COMMANDS */
    shared_ptr<CeilingFanOneStateCommand> _commandCeilingFanStateOne = make_shared<CeilingFanOneStateCommand>(_ceilingFan);
    shared_ptr<CeilingFanTwoStateCommand> _commandCeilingFanStateTwo = make_shared<CeilingFanTwoStateCommand>(_ceilingFan);
    shared_ptr<CeilingFanThreeStateCommand> _commandCeilingFanStateThree = make_shared<CeilingFanThreeStateCommand>(_ceilingFan);
    shared_ptr<CeilingFanFourStateCommand> _commandCeilingFanStateFour = make_shared<CeilingFanFourStateCommand>(_ceilingFan);
    shared_ptr<CeilingFanFiveStateCommand> _commandCeilingFanStateFive = make_shared<CeilingFanFiveStateCommand>(_ceilingFan);
    shared_ptr<CeilingFanOffCommand> _commandCeilingFanOff = make_shared<CeilingFanOffCommand>(_ceilingFan);

    /* Setting command to invocer */
    remote->setCommand(1, _commandCeilingFanStateOne, _commandCeilingFanOff);
    remote->setCommand(2, _commandCeilingFanStateTwo, _commandCeilingFanOff);
    remote->setCommand(3, _commandCeilingFanStateThree, _commandCeilingFanOff);
    remote->setCommand(4, _commandCeilingFanStateFour, _commandCeilingFanOff);
    remote->setCommand(5, _commandCeilingFanStateFive, _commandCeilingFanOff);

    /* Execitomg commands */
    remote->onButtonPress(5);
    remote->offButtonPress(5);
    remote->undoButtonPress();

}