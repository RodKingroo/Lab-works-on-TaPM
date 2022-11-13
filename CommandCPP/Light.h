/* Copyright (c) 2022 RodKingroo */
#pragma once
using namespace std;

static enum class RoomState
{
	UNKNOWN,
	HALLWAY,
	LIVINROOM,
	BEDROOM,
	KITCHEN,
	BATHROOM,
	STOREROOM,
	GARAGE,
};

class Light
{
	RoomState state = RoomState::UNKNOWN;
public:
	void on();
	void off();

	void setHallway();
	void setLivinRoom();
	void setBedRoom();
	void setKitchen();
	void setBathRoom();
	void setStoreRoom();
	void setGarage();

	RoomState getRoom();

};

