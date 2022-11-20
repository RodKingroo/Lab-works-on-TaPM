#include "StereoCommand.h"
#include <memory>

/* Stereo On With CD Command */
StereoOnWithCDCommand::StereoOnWithCDCommand(std::shared_ptr<Stereo> stereo) 
{ 
	this->stereo = stereo;
}

void StereoOnWithCDCommand::execute()
{
	stereo->on();
	stereo->setCD();
	stereo->setVolume(11);

}

void StereoOnWithCDCommand::undo()
{
	stereo->off();
}

/* Stereo On With DVD Command */
StereoOnWithDVDCommand::StereoOnWithDVDCommand(std::shared_ptr<Stereo> stereo)
{
	this->stereo = stereo;
}

void StereoOnWithDVDCommand::execute()
{
	stereo->on();
	stereo->setDVD();
	stereo->setVolume(11);

}

void StereoOnWithDVDCommand::undo()
{
	stereo->off();
}

/* Stereo On With Radio Command */
StereoOnWithRadioCommand::StereoOnWithRadioCommand(std::shared_ptr<Stereo> stereo) 
{ 
	this->stereo = stereo; 
}

void StereoOnWithRadioCommand::execute()
{
	stereo->on();
	stereo->setRadio();
	stereo->setVolume(15);

}

void StereoOnWithRadioCommand::undo()
{
	stereo->off();

}

/* Stereo Off Command */
StereoOffCommand::StereoOffCommand(std::shared_ptr<Stereo> stereo) 
{ 
	this->stereo = stereo; 
}

void StereoOffCommand::execute()
{
	prevVolume = stereo->getVolume();
	prevState = stereo->getState();
	stereo->off();

}

void StereoOffCommand::undo(){
	stereo->on();
	switch (prevState) {
	case StereoState::CD:
		stereo->setCD();
		break;
	case StereoState::DVD:
		stereo->setDVD();
		break;
	case StereoState::RADIO:
		stereo->setRadio();
		break;
	}
	stereo->setVolume(prevVolume);
}