/* Copyright (c) 2022 RodKingroo */
#pragma once
#include <iostream>
#include "HouseDoor.h"
#include "Command.h"

using namespace std;

class HouseDoorOpenCommand : public Command
{
private:
    shared_ptr<HouseDoor> houseDoor;
public:
    HouseDoorOpenCommand(shared_ptr<HouseDoor> garageDoor);
    void execute() override;
    void undo() override;
};

class HouseDoorCloseCommand : public Command
{
private:
    shared_ptr<HouseDoor> houseDoor;
public:
    HouseDoorCloseCommand(shared_ptr<HouseDoor> garageDoor);
    void execute() override;
    void undo() override;
};