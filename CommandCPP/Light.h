#pragma once
using namespace std;

class Light
{
	int state = OFF;
public:
	void on();
	void off();

	void state_1();
	void state_2();
	void state_3();
	void state_4();
	void state_5();

	const int getState();


	static enum
	{
		OFF = 0,
		STAGE_ONE = 20,
		STAGE_TWO = 40,
		STAGE_THREE = 60,
		STAGE_FOUR = 80,
		STAGE_FIVE = 100,

	};

};

