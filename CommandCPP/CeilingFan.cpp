#include "CeilingFan.h"



void CeilingFan::high()
{
	speed = High;
	std::cout << "Ceiling Fan Speed " << speed << std::endl;
}

void CeilingFan::medium()
{
	speed = Medium;
	std::cout << "Ceiling Fan Speed " << speed << std::endl;
}

void CeilingFan::low()
{
	speed = Low;
	std::cout << "Ceiling Fan Speed " << speed << std::endl;

}

void CeilingFan::off()
{
	speed = Off;
	std::cout << "Ceiling Fan Speed " << speed << std::endl;

}

const int CeilingFan::getSpeed()
{
	return speed;
}