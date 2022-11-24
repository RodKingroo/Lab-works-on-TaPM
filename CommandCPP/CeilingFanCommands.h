#pragma once
#include "Command.h"
#include "CeilingFan.h"
#include <memory>

void setUndo(std::shared_ptr<CeilingFan> ceilingFan, int prevSpeed);

class CeilingFanStateOneCommand : public Command 
{
	std::shared_ptr<CeilingFan> ceilingFan;
	int prevSpeed;
public:
	CeilingFanStateOneCommand(std::shared_ptr<CeilingFan> ceilingFan);
	void execute() override;
	void undo();

};

class CeilingFanStateTwoCommand : public Command 
{
	std::shared_ptr<CeilingFan> ceilingFan;
	int prevSpeed;
public:
	CeilingFanStateTwoCommand(std::shared_ptr<CeilingFan> ceilingFan);
	void execute() override;
	void undo();

};

class CeilingFanStateThreeCommand : public Command 
{
	std::shared_ptr<CeilingFan> ceilingFan;
	int prevSpeed;
public:
	CeilingFanStateThreeCommand(std::shared_ptr<CeilingFan> ceilingFan);
	void execute() override;
	void undo();

};

class CeilingFanStateFourCommand : public Command 
{
	std::shared_ptr<CeilingFan> ceilingFan;
	int prevSpeed;
public:
	CeilingFanStateFourCommand(std::shared_ptr<CeilingFan> ceilingFan);
	void execute() override;
	void undo();

};

class CeilingFanStateFiveCommand : public Command 
{
	std::shared_ptr<CeilingFan> ceilingFan;
	int prevSpeed;
public:
	CeilingFanStateFiveCommand(std::shared_ptr<CeilingFan> ceilingFan);
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