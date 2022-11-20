#pragma once
#include "Command.h"
#include "Light.h"
#include <memory>
class LightOnCommand : public Command
{
	std::shared_ptr<Light> light;
public:
	LightOnCommand(std::shared_ptr<Light> light);
	void execute()override;
	void undo() override;
};

class LightOffCommand : public Command {
	std::shared_ptr<Light>light;
public:
	LightOffCommand(std::shared_ptr<Light> light);
	void execute() override;
	void undo() override;

};

