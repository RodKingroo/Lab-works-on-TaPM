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
	std::shared_ptr<Light> bedRoomLight = std::make_shared<Light>();
	std::shared_ptr<CeilingFan> bedRoomCeilingFan = std::make_shared<CeilingFan>();
	std::shared_ptr<Stereo> stereo = std::make_shared<Stereo>();

	/* Command pattern COMMANDS */
	std::shared_ptr<LightOnCommand> livingRoomLightOn = std::make_shared<LightOnCommand>(livingRoomLight);
	std::shared_ptr<LightOffCommand> livingRoomLightOff = std::make_shared<LightOffCommand>(livingRoomLight);

	std::shared_ptr<LightOnCommand> bedRoomLightOn = std::make_shared<LightOnCommand>(bedRoomLight);
	std::shared_ptr<LightOffCommand> bedRoomLightOff = std::make_shared<LightOffCommand>(bedRoomLight);

	std::shared_ptr<CeilingFanHighCommand> ceilingFanHigh = std::make_shared<CeilingFanHighCommand>(bedRoomCeilingFan);
	std::shared_ptr<CeilingFanMediumCommand> ceilingFanMedium = std::make_shared<CeilingFanMediumCommand>(bedRoomCeilingFan);
	std::shared_ptr<CeilingFanLowCommand> ceilingFanLow = std::make_shared <CeilingFanLowCommand> (bedRoomCeilingFan);
	std::shared_ptr<CeilingFanOffCommand> ceilingFanOff = std::make_shared<CeilingFanOffCommand>(bedRoomCeilingFan);

	std::shared_ptr<StereoOnWithCDCommand> stereoCD = std::make_shared<StereoOnWithCDCommand>(stereo);
	std::shared_ptr<StereoOnWithRadioCommand> stereoRadio = std::make_shared<StereoOnWithRadioCommand>(stereo);
	std::shared_ptr<StereoOffCommand> stereoOff = std::make_shared<StereoOffCommand>(stereo);

	/* Setting command to invocer */
	remote->setCommand(0, livingRoomLightOn, livingRoomLightOff);
	remote->setCommand(1, bedRoomLightOn, bedRoomLightOff);
	remote->setCommand(2, ceilingFanHigh, ceilingFanOff);
	remote->setCommand(3, ceilingFanMedium, ceilingFanOff);
	remote->setCommand(4, ceilingFanLow, ceilingFanOff);
	remote->setCommand(5, stereoCD, stereoOff);
	remote->setCommand(6, stereoRadio, stereoOff);

	/* Execitomg commands */
	remote->onButtonPress(0);
	remote->offButtonPress(0);
	remote->undoButtonPress();

	remote->onButtonPress(2);
	remote->offButtonPress(2);
	remote->undoButtonPress();

	remote->onButtonPress(5);
	remote->offButtonPress(5);
	remote->undoButtonPress();

	return 0;

}