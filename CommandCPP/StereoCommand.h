#pragma once
#include "Command.h"
#include "Stereo.h"
class StereoOnWithCDCommand : public Command 
{
	std::shared_ptr<Stereo> stereo = nullptr;
public:
	StereoOnWithCDCommand(std::shared_ptr<Stereo> stereo);
	void execute() override;
	void undo() override;
};

class StereoOnWithDVDCommand : public Command
{
	std::shared_ptr<Stereo> stereo = nullptr;
public:
	StereoOnWithDVDCommand(std::shared_ptr<Stereo> stereo);
	void execute() override;
	void undo() override;

};

class StereoOnWithRadioCommand : public Command
{
	std::shared_ptr<Stereo> stereo = nullptr;
public:
	StereoOnWithRadioCommand(std::shared_ptr<Stereo> stereo);
	void execute() override;
	void undo() override;
};

class StereoOnWithCloudCommand : public Command
{
	std::shared_ptr<Stereo> stereo = nullptr;
public:
	StereoOnWithCloudCommand(std::shared_ptr<Stereo> stereo);
	void execute() override;
	void undo() override;

};

class StereoOffCommand : public Command
{
	std::shared_ptr<Stereo> stereo = nullptr;
	int prevVolume = 0;
	StereoState prevState = StereoState::UNKNOWN;
public:
	StereoOffCommand(std::shared_ptr<Stereo> stereo);
	void execute() override;
	void undo() override;
};

class StereoOnCommand : public Command
{
	std::shared_ptr<Stereo> stereo = nullptr;
	int prevVolume = 0;
	StereoState prevState = StereoState::UNKNOWN;
public:
	StereoOnCommand(std::shared_ptr<Stereo> stereo);
	void execute() override;
	void undo() override;
};

