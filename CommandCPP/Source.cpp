#include "RemoteControl.h"
#include "Light.h"
#include "Stereo.h"
#include "CeilingFan.h"
#include "LightCommand.h"
#include "StereoCommand.h"
#include "CeilingFanCommands.h"

/* Command pattern CLIENT */
int main() {
	/* Command pattern INVOKER */
	std::unique_ptr<RemoteControl> remote = std::make_unique<RemoteControl>();
	
	/* Command pattern RECEIVERS */
	std::shared_ptr<Light> livingRoomLight = std::make_shared<Light>();
	std::shared_ptr<CeilingFan> bedRoomCeilingFan = std::make_shared<CeilingFan>();
	std::shared_ptr<Stereo> stereo = std::make_shared<Stereo>();

	/* Command pattern COMMANDS */
	std::shared_ptr<StereoOnWithCDCommand> stereoCD = std::make_shared<StereoOnWithCDCommand>(stereo);
	std::shared_ptr<StereoOffCommand> stereoOff = std::make_shared<StereoOffCommand>(stereo);

	/* Setting command to invocer */
	remote->setCommand(3, stereoCD, stereoOff);

	/* Execitomg commands */
	remote->onButtonPress(1);
	remote->offButtonPress(1);
	remote->undoButtonPress();

	return 0;

}