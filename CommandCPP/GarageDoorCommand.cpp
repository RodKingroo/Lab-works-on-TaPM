/* Copyright (c) 2022 RodKingroo */
#include "GarageDoorCommand.h"

GarageDoorOpenCommand::GarageDoorOpenCommand(shared_ptr<GarageDoor> garageDoor)
{
    this->garageDoor = garageDoor;
}

void GarageDoorOpenCommand::execute() /* override */
{
    garageDoor->open();
}

void GarageDoorOpenCommand::undo() /* override */
{
    garageDoor->close();
}

GarageDoorCloseCommand::GarageDoorCloseCommand(shared_ptr<GarageDoor> garageDoor)
{
    this->garageDoor = garageDoor;
}

void GarageDoorCloseCommand::execute() /* override */
{
    garageDoor->close();
}

void GarageDoorCloseCommand::undo() /* override */
{
    garageDoor->open();
}
