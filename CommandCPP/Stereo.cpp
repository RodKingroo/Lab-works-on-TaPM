#include "Stereo.h"

void Stereo::on()
{
	std::cout << "Stereo on" << std::endl;

}

void Stereo::off()
{
	std::cout << "Stereo off" << std::endl;

}

void Stereo::setCD()
{
	std::cout << "CD setted" << std::endl;
	state = StereoState::CD;
}

void Stereo::setDVD()
{
	std::cout << "DVD setted" << std::endl;
	state = StereoState::DVD;
}

void Stereo::setRadio()
{
	std::cout << "Radio setted" << std::endl;
	state = StereoState::RADIO;
}

void Stereo::setCloudMusic() 
{
	std::cout << "Cload music setted" << std::endl;
	state = StereoState::CLOUD_MUSIC;
}


void Stereo::setVolume(int volume)
{
	this->volume = volume;
	std::cout << "setted volume " << volume << std::endl;
}

int Stereo::getVolume() {
	return volume; 

}

StereoState Stereo::getState() {
	return state;

}