/* Copyright (c) 2022 RodKingroo */
#pragma once
#include <memory>
#include <vector>
#include "Command.h"
#include "NoCommand.h"
class RemoteControl
{
	std::vector <std::shared_ptr<Command>> onCommands;
	std::vector <std::shared_ptr<Command>> offCommands;
	std::shared_ptr<Command> undoCommand = nullptr;
public:
	RemoteControl();
	void setCommand(int slot, std::shared_ptr<Command> onCommand, std::shared_ptr<Command> offCommand);
	void onButtonPress(int slot);
	void offButtonPress(int slot);
	void undoButtonPress();

};

