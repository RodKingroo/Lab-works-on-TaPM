#pragma once
#include "Command.h"
#include "CeilingFan.h"
#include <memory>

void setUndo(std::shared_ptr<CeilingFan> ceilingFan, int prevSpeed);

class CeilingFanHighCommand : public Command 
{
	std::shared_ptr<CeilingFan> ceilingFan;
	int prevSpeed;
public:
	CeilingFanHighCommand(std::shared_ptr<CeilingFan> ceilingFan);
	void execute() override;
	void undo();

};

class CeilingFanMediumCommand : public Command
{
	std::shared_ptr<CeilingFan> ceilingFan;
	int prevSpeed;
public:
	CeilingFanMediumCommand(std::shared_ptr<CeilingFan> ceilingFan);
	void execute() override;
	void undo();
};

class CeilingFanLowCommand : public Command
{
	std::shared_ptr<CeilingFan> ceilingFan;
	int prevSpeed;
public:
	CeilingFanLowCommand(std::shared_ptr<CeilingFan> ceilingFan);
	void execute() override;
	void undo();
};

class CeilingFanOffCommand : public Command
{
	std::shared_ptr<CeilingFan> ceilingFan;
	int prevSpeed;
public:
	CeilingFanOffCommand(std::shared_ptr<CeilingFan> ceilingFan);
	void execute() override;
	void undo();
};