#pragma once
#include <iostream>

class GarageDoor
{
	void up() { std::cout << "Garage Door Up" << std::endl; }
	void down(){ std::cout << "Garage Door Down" << std::endl; }
	void stop(){ std::cout << "Garage Door Stoped" << std::endl; }
	void lighton(){ std::cout << "Garage Light On" << std::endl; }
	void lightOff(){ std::cout << "Garage light Off" << std::endl; }

};

