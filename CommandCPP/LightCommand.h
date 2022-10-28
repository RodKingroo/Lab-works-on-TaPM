#pragma once
#include "Command.h"
#include "Light.h"
class LightOnCommand : public Command
{
	std::shared_ptr<Light> light;
public:
	LightOnCommand(std::shared_ptr<Light> light) { this->light = light; }
	void execute()override { light->on(); }
	void undo() override { light->off(); }
};

class LightOffCommand : public Command {
	std::shared_ptr<Light>light;
public:
	LightOffCommand(std::shared_ptr<Light> light) { this->light = light; }
	void execute() override { light->off(); }
	void undo() override { light->on(); }

};

