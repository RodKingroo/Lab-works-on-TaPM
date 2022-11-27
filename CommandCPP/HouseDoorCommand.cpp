/* Copyright (c) 2022 RodKingroo */
#include "HouseDoorCommand.h"

HouseDoorOpenCommand::HouseDoorOpenCommand(shared_ptr<HouseDoor> garageDoor)
{
    this->houseDoor = garageDoor;
}

void HouseDoorOpenCommand::execute() /* override */
{
    houseDoor->open();
}

void HouseDoorOpenCommand::undo() /* override */
{
    houseDoor->close();
}

HouseDoorCloseCommand::HouseDoorCloseCommand(shared_ptr<HouseDoor> garageDoor)
{
    this->houseDoor = garageDoor;
}

void HouseDoorCloseCommand::execute() /* override */
{
    houseDoor->close();
}

void HouseDoorCloseCommand::undo() /* override */
{
    houseDoor->open();
}
