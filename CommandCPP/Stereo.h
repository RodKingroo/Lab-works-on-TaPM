#pragma once
#include <iostream>

static enum class StereoState 
{
	UNKNOWN = 0,
	CD = 1,
	DVD = 2,
	RADIO = 3,
	CLOUD_MUSIC = 4,


};

class Stereo
{
	int volume = 0;
	StereoState state = StereoState::UNKNOWN;
public:
	void on();
	void off();

	void setCD();
	void setDVD();
	void setRadio();
	void setCloudMusic();

	void setVolume(int volume);
	int getVolume();
	StereoState getState();

};

