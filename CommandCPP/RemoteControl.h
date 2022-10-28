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
	RemoteControl() {
		std::shared_ptr<Command> noCommand = std::make_shared<NoCommand>();
		for (int i = 0; i < 7; i++) {
			onCommands.push_back(noCommand);
			offCommands.push_back(noCommand);
		}
		undoCommand = noCommand;

	}

	void setCommand(int slot, std::shared_ptr<Command> onCommand, std::shared_ptr<Command> offCommand)
	{
		onCommands[slot] = onCommand;
		offCommands[slot] = onCommand;
	}

	void onButtonPress(int slot) {
		onCommands[slot]->execute();
		undoCommand = onCommands[slot];
	}

	void offButtonPress(int slot) {
		offCommands[slot]->execute();
		undoCommand = offCommands[slot];
	}

	void undoButtonPress() {
		undoCommand->undo();
	}

};

