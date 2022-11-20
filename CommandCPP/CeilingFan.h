#pragma once
#include <iostream>

class CeilingFan
{
private:
	int speed = 0;
public:
	void high();
	void medium();
	void low();
	void off();
	const int getSpeed();

	static enum {
		High = 3,
		Medium = 2,
		Low = 1,
		Off = 0, 
	};
};