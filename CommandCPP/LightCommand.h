/* Copyright (c) 2022 RodKingroo */
#pragma once
#include "Command.h";
#include "Light.h"
#include <iostream>;

using namespace std;

class LightOnInHallway : public Command
{
	shared_ptr<Light> light = nullptr;
public:
	LightOnInHallway(shared_ptr<Light> light);
	void execute() override;
	void undo() override;

};

class LightOnInLivinroom : public Command
{
	shared_ptr<Light> light = nullptr;
public:
	LightOnInLivinroom(shared_ptr<Light> light);
	void execute() override;
	void undo() override;

};

class LightOnInBedroom : public Command
{
	shared_ptr<Light> light = nullptr;
public:
	LightOnInBedroom(shared_ptr<Light> light);
	void execute() override;
	void undo() override;

};

class LightOnInKitchen : public Command
{
	shared_ptr<Light> light = nullptr;
public:
	LightOnInKitchen(shared_ptr<Light> light);
	void execute() override;
	void undo() override;

};

class LightOnInBathRoom : public Command
{
	shared_ptr<Light> light = nullptr;
public:
	LightOnInBathRoom(shared_ptr<Light> light);
	void execute() override;
	void undo() override;

};

class LightOnInStoreRoom : public Command
{
	shared_ptr<Light> light = nullptr;
public:
	LightOnInStoreRoom(shared_ptr<Light> light);
	void execute() override;
	void undo() override;

};

class LightOnInGarage : public Command
{
	shared_ptr<Light> light = nullptr;
public:
	LightOnInGarage(shared_ptr<Light> light);
	void execute() override;
	void undo() override;

};