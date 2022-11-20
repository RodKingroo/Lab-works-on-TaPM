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


void Light::getHallway() 
{
	cout << "Hallway light selected" << endl;
	state = RoomState::HALLWAY;

}

void Light::getLivinRoom() 
{
	cout << "LivinRoom light selected" << endl;
	state = RoomState::LIVINROOM;

}

void Light::getBedRoom() 
{
	cout << "Bed Room light selected" << endl;
	state = RoomState::BEDROOM;

}

void Light::getKitchen() 
{
	cout << "Kitchen light selected" << endl;
	state = RoomState::KITCHEN;

}

void Light::getBathRoom() 
{
	cout << "Bath Room light selected" << endl;
	state = RoomState::BATHROOM;

}

void Light::getStoreRoom() 
{
	cout << "Store Room light selected" << endl;
	state = RoomState::STOREROOM;

}

void Light::getGarage() 
{
	cout << "Garage Room light selected" << endl;
	state = RoomState::GARAGE;

}

RoomState Light::getRoom() 
{
	return state;

}