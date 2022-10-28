#pragma once
#include <iostream>

static enum class StereoState 
{
	CD = 0,
	DVD = 1,
	RADIO = 3,

};

class Stereo
{
	int volume = 0;
	StereoState state = StereoState::RADIO;
public:
	void on() { std::cout << "Stereo on" << std::endl; }
	void off(){ std::cout << "Stereo off" << std::endl; }
	
	void setCD()
	{
		std::cout << "CD setted" << std::endl;
		state = StereoState::CD;
	}

	void setDVD()
	{
		std::cout << "DVD setted" << std::endl;
		state = StereoState::DVD;
	}

	void setRadio()
	{
		std::cout << "Radio setted" << std::endl;
		state = StereoState::RADIO;
	}

	void setVolume(int volume)
	{
		this->volume = volume;
		std::cout << "setted volume" << volume << std::endl;
	}

	int getVolume() { return volume; }
	StereoState getState() { return state; }

};

