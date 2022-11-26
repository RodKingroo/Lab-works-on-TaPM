#pragma once
#include <iostream>

using namespace std;

class CeilingFan
{
private:
	int speed = OFF;
public:
	void on();
	void off();

	void state_1();
	void state_2();
	void state_3();
	void state_4();
	void state_5();
	const int getState();

    static enum{
        OFF = 0,
        STATE_ONE = 1,
        STATE_TWO = 2,
        STATE_THREE = 4,
        STATE_FOUR = 8,
        STATE_FIVE = 16,
    };

};