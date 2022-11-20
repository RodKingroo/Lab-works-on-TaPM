#include "LightCommand.h"

/* Light On Command */
LightOnCommand::LightOnCommand(std::shared_ptr<Light> light) 
{ 
	this->light = light; 
}

void LightOnCommand::execute()
{ 
	light->on(); 
}

void LightOnCommand::undo()
{ 
	light->off(); 
}


/* Light Off Command */
LightOffCommand::LightOffCommand(std::shared_ptr<Light> light)
{ 
	this->light = light; 
}

void LightOffCommand::execute() 
{ 
	light->off(); 
}

void LightOffCommand::undo()
{ 
	light->on(); 
}