#pragma once
#include "Command.h"
#include "CeilingFan.h"

void setUndo(std::shared_ptr<CeilingFan> ceilingFan, int prevSpeed) 
{
	switch (prevSpeed) 
	{
	case CeilingFan::High:
		ceilingFan->high();
		break;
	case CeilingFan::Medium:
		ceilingFan->medium();
		break;
	case CeilingFan::Low:
		ceilingFan->low();
		break;
	case CeilingFan::Off:
		ceilingFan->off();
		break;
	}
}

class CeilingFanHighCommand : public Command 
{
	std::shared_ptr<CeilingFan> ceilingFan;
	int prevSpeed;
public:
	CeilingFanHighCommand(std::shared_ptr<CeilingFan> ceilingFan) { this->ceilingFan = ceilingFan; }
	void execute() override 
	{
		prevSpeed = ceilingFan->getSpeed();
		ceilingFan->high();
	}
	void undo() {
		setUndo(ceilingFan, prevSpeed);

	}
};

class CeilingFanMediumCommand : public Command
{
	std::shared_ptr<CeilingFan> ceilingFan;
	int prevSpeed;
public:
	CeilingFanMediumCommand(std::shared_ptr<CeilingFan> ceilingFan) { this->ceilingFan = ceilingFan; }
	void execute() override
	{
		prevSpeed = ceilingFan->getSpeed();
		ceilingFan->medium();
	}
	void undo() 
	{
		setUndo(ceilingFan, prevSpeed);

	}
};

class CeilingFanLowCommand : public Command
{
	std::shared_ptr<CeilingFan> ceilingFan;
	int prevSpeed;
public:
	CeilingFanLowCommand(std::shared_ptr<CeilingFan> ceilingFan) { this->ceilingFan = ceilingFan; }
	void execute() override
	{
		prevSpeed = ceilingFan->getSpeed();
		ceilingFan->low();
	}
	void undo() 
	{
		setUndo(ceilingFan, prevSpeed);

	}
};

class CeilingFanOffCommand : public Command
{
	std::shared_ptr<CeilingFan> ceilingFan;
	int prevSpeed;
public:
	CeilingFanOffCommand(std::shared_ptr<CeilingFan> ceilingFan) { this->ceilingFan = ceilingFan; }
	void execute() override
	{
		prevSpeed = ceilingFan->getSpeed();
		ceilingFan->off();
	}
	void undo() 
	{
		setUndo(ceilingFan, prevSpeed);

	}
};