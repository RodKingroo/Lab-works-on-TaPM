/* Copyright (c) 2022 RodKingroo */
#include <iostream>
#include <vector>

#include "CeilingFan.h"
#include "Command.h"

using namespace std;

class CeilingFanOffCommand : public Command
{
private:
    shared_ptr<CeilingFan> ceilingFan;
    int prevSpeed;
public:
    CeilingFanOffCommand(shared_ptr<CeilingFan> ceilingFan);
    void execute() override;
    void undo() override;

};

class CeilingFanOneStateCommand : public Command
{
private:
    shared_ptr<CeilingFan> ceilingFan;
    int prevSpeed;
public:
    CeilingFanOneStateCommand(shared_ptr<CeilingFan> ceilingFan);
    void execute() override;
    void undo() override;

};

class CeilingFanTwoStateCommand : public Command
{
private:
    shared_ptr<CeilingFan> ceilingFan;
    int prevSpeed;
public:
    CeilingFanTwoStateCommand(shared_ptr<CeilingFan> ceilingFan);
    void execute() override;
    void undo() override;

};

class CeilingFanThreeStateCommand : public Command
{
private:
    shared_ptr<CeilingFan> ceilingFan;
    int prevSpeed;
public:
    CeilingFanThreeStateCommand(shared_ptr<CeilingFan> ceilingFan);
    void execute() override;
    void undo() override;

};

class CeilingFanFourStateCommand : public Command
{
private:
    shared_ptr<CeilingFan> ceilingFan;
    int prevSpeed;
public:
    CeilingFanFourStateCommand(shared_ptr<CeilingFan> ceilingFan);
    void execute() override;
    void undo() override;

};

class CeilingFanFiveStateCommand : public Command
{
private:
    shared_ptr<CeilingFan> ceilingFan;
    int prevSpeed;
public:
    CeilingFanFiveStateCommand(shared_ptr<CeilingFan> ceilingFan);
    void execute() override;
    void undo() override;

};