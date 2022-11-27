/* Copyright (c) 2022 RodKingroo */
#include <iostream>
#include "Command.h"
#include "StreetLight.h"

using namespace std;

/* Street Light On State One Command */
class StreetLightOnStateOneCommand : public Command
{
private:
    shared_ptr<StreetLight> light;
    int prevBright;
public:
    StreetLightOnStateOneCommand(shared_ptr<StreetLight> light);
    void execute() override;
    void undo() override;

};

/* Street Light On State Two Command */
class StreetLightOnStateTwoCommand : public Command
{
private:
    shared_ptr<StreetLight> light;
    int prevBright;
public:
    StreetLightOnStateTwoCommand(shared_ptr<StreetLight> light);
    void execute() override;
    void undo() override;

};

/* Street Light On State Three Command */
class StreetLightOnStateThreeCommand : public Command
{
private:
    shared_ptr<StreetLight> light;
    int prevBright;
public:
    StreetLightOnStateThreeCommand(shared_ptr<StreetLight> light);
    void execute() override;
    void undo() override;

};

/* Street Light On State Four Command */
class StreetLightOnStateFourCommand : public Command
{
private:
    shared_ptr<StreetLight> light;
    int prevBright;
public:
    StreetLightOnStateFourCommand(shared_ptr<StreetLight> light);
    void execute() override;
    void undo() override;

};

/* Street Light On State Five Command */
class StreetLightOnStateFiveCommand : public Command
{
private:
    shared_ptr<StreetLight> light;
    int prevBright;
public:
    StreetLightOnStateFiveCommand(shared_ptr<StreetLight> light);
    void execute() override;
    void undo() override;

};

/* Street Light Off Command */
class StreetLightOffCommand : public Command
{
private:
    shared_ptr<StreetLight> light;
    int prevBright;
public:
    StreetLightOffCommand(shared_ptr<StreetLight> light);
    void execute() override;
    void undo() override;

};