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

	void getHallway();
	void getLivinRoom();
	void getBedRoom();
	void getKitchen();
	void getBathRoom();
	void getStoreRoom();
	void getGarage();

	RoomState getRoom();

};

