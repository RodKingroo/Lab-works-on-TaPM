/* Copyright (c) 2022 RodKingroo */
#pragma once
#include "Command.h"
#include "Stereo.h"

#include <iostream>

using namespace std;

class StereoOnCassetteCommand : public Command
{
private:
    shared_ptr<Stereo> stereo;
    int prevType;
public:
    StereoOnCassetteCommand(shared_ptr<Stereo> stereo);
    void execute() override;
    void undo() override;

};

class StereoOnCDCommand : public Command
{
private:
    shared_ptr<Stereo> stereo;
    int prevType;
public:
    StereoOnCDCommand(shared_ptr<Stereo> stereo);
    void execute() override;
    void undo() override;

};

class StereoOnDVDCommand : public Command
{
private:
    shared_ptr<Stereo> stereo;
    int prevType;
public:
    StereoOnDVDCommand(shared_ptr<Stereo> stereo);
    void execute() override;
    void undo() override;

};

class StereoOnRadioCommand : public Command
{
private:
    shared_ptr<Stereo> stereo;
    int prevType;
public:
    StereoOnRadioCommand(shared_ptr<Stereo> stereo);
    void execute() override;
    void undo() override;

};

class StereoOnCloudCommand : public Command
{
private:
    shared_ptr<Stereo> stereo;
    int prevType;
public:
    StereoOnCloudCommand(shared_ptr<Stereo> stereo);
    void execute() override;
    void undo() override;

};

class StereoOffCommand : public Command
{
private:
    shared_ptr<Stereo> stereo;
    int prevType;
public:
    StereoOffCommand(shared_ptr<Stereo> stereo);
    void execute() override;
    void undo() override;

};