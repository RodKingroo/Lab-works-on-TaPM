/* Copyright (c) 2022 RodKingroo */
#include "RemoteControl.h"

RemoteControl::RemoteControl() 
{
	std::shared_ptr<Command> noCommand = std::make_shared<NoCommand>();
	for (int i = 0; i < 37; i++) {
		onCommands.push_back(noCommand);
		offCommands.push_back(noCommand);
	}
	
	undoCommand = noCommand;

}

void RemoteControl::setCommand(int slot, std::shared_ptr<Command> onCommand, std::shared_ptr<Command> offCommand)
{
	onCommands[slot] = onCommand;
	offCommands[slot] = offCommand;
}

void RemoteControl::onButtonPress(int slot) {
	onCommands[slot]->execute();
	undoCommand = onCommands[slot];
}

void RemoteControl::offButtonPress(int slot) {
	offCommands[slot]->execute();
	undoCommand = offCommands[slot];

}

void RemoteControl::undoButtonPress() {
	undoCommand->undo();
}