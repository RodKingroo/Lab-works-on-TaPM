/* Copyright (c) 2022 RodKingroo */
#pragma once
#include <iostream>
#include "GarageDoor.h"
#include "Command.h"

using namespace std;

class GarageDoorOpenCommand : public Command
{
private:
    shared_ptr<GarageDoor> garageDoor;
public:
    GarageDoorOpenCommand(shared_ptr<GarageDoor> garageDoor);
    void execute() override;
    void undo() override;
};

class GarageDoorCloseCommand : public Command
{
private:
    shared_ptr<GarageDoor> garageDoor;
public:
    GarageDoorCloseCommand(shared_ptr<GarageDoor> garageDoor);
    void execute() override;
    void undo() override;
};