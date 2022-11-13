/* Copyright (c) 2022 RodKingroo */

#include "Light.h"
#include <iostream>

void Light::on() 
{
	cout << "Light is on" << endl;

}

void Light::off() 
{
	cout << "Light is off" << endl;

}


void Light::setHallway() 
{
	cout << "Hallway light selected" << endl;
	state = RoomState::HALLWAY;

}

void Light::setLivinRoom() 
{
	cout << "LivinRoom light selected" << endl;
	state = RoomState::LIVINROOM;

}

void Light::setBedRoom() 
{
	cout << "Bed Room light selected" << endl;
	state = RoomState::BEDROOM;

}

void Light::setKitchen() 
{
	cout << "Kitchen light selected" << endl;
	state = RoomState::KITCHEN;

}

void Light::setBathRoom() 
{
	cout << "Bath Room light selected" << endl;
	state = RoomState::BATHROOM;

}

void Light::setStoreRoom() 
{
	cout << "Store Room light selected" << endl;
	state = RoomState::STOREROOM;

}

void Light::setGarage() 
{
	cout << "Garage Room light selected" << endl;
	state = RoomState::GARAGE;

}

RoomState Light::getRoom() 
{
	return state;

}