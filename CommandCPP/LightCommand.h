/* Copyright (c) 2022 RodKingroo */
#pragma once
#include <iostream>
#include "Command.h"
#include "Light.h"

using namespace std;

/* Light On State One Command */
class LightOnStateOneCommand : public Command
{
private:
    shared_ptr<Light> light;
    int prevBright;
public:
    LightOnStateOneCommand(shared_ptr<Light> light);
    void execute() override;
    void undo() override;

};

/* Light On State Two Command */
class LightOnStateTwoCommand : public Command
{
private:
    shared_ptr<Light> light;
    int prevBright;
public:
    LightOnStateTwoCommand(shared_ptr<Light> light);
    void execute() override;
    void undo() override;

};

/* Light On State Three Command */
class LightOnStateThreeCommand : public Command
{
private:
    shared_ptr<Light> light;
    int prevBright;
public:
    LightOnStateThreeCommand(shared_ptr<Light> light);
    void execute() override;
    void undo() override;

};

/* Light On State Four Command */
class LightOnStateFourCommand : public Command
{
private:
    shared_ptr<Light> light;
    int prevBright;
public:
    LightOnStateFourCommand(shared_ptr<Light> light);
    void execute() override;
    void undo() override;

};

/* Light On State Five Command */
class LightOnStateFiveCommand : public Command
{
private:
    shared_ptr<Light> light;
    int prevBright;
public:
    LightOnStateFiveCommand(shared_ptr<Light> light);
    void execute() override;
    void undo() override;

};

/* Light Off Command */
class LightOffCommand : public Command
{
private:
    shared_ptr<Light> light;
    int prevBright;
public:
    LightOffCommand(shared_ptr<Light> light);
    void execute() override;
    void undo() override;

};