#pragma once
#include <iostream>

class CeilingFan
{
	int speed = 0;
public:
	static enum {
		High = 3,
		Medium = 2,
		Low = 1,
		Off = 0,
	};

	void high() 
	{
		speed = High;
		std::cout << "Ceiling Fan Speed " << speed << std::endl;
	}

	void medium()
	{
		speed = Medium;
		std::cout << "Ceiling Fan Speed " << speed << std::endl;
	}

	void low()
	{
		speed = Low;
		std::cout << "Ceiling Fan Speed " << speed << std::endl;

	}

	void off()
	{
		speed = Off;
		std::cout << "Ceiling Fan Speed " << speed << std::endl;

	}

	const int getSpeed() { return speed; }

};

