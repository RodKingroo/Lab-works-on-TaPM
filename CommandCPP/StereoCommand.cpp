/* Copyright (c) 2022 RodKingroo */
#include "StereoCommand.h"

void setUndo(shared_ptr<Stereo> stereo, int prevType)
{
    switch (prevType)
    {
    case Stereo::UNKNOWN:
        stereo->setVolume(0);
        break;
    case Stereo::CASSETTE:
        stereo->setCassette();
        stereo->setVolume(10);
        break;
    case Stereo::CD:
        stereo->setCD();
        stereo->setVolume(5);
        break;
    case Stereo::DVD:
        stereo->setDVD();
        stereo->setVolume(15);
        break;
    case Stereo::RADIO:
        stereo->setRadio();
        stereo->setVolume(30);
        break;
    case Stereo::CLOUDMUSIC:
        stereo->setCloud();
        stereo->setVolume(50);
        break;
    }

}


/* Stereo On Cassette Command */
StereoOnCassetteCommand::StereoOnCassetteCommand(shared_ptr<Stereo> stereo)
{
    this->stereo = stereo;
}

void StereoOnCassetteCommand::execute() /* override */
{
    prevType = stereo->getState();
    stereo->on();
    stereo->setCassette();
    stereo->setVolume(10);

}

void StereoOnCassetteCommand::undo() /* override */
{
    stereo->off();
    setUndo(stereo, prevType);

}


/* Stereo On CD Command */
StereoOnCDCommand::StereoOnCDCommand(shared_ptr<Stereo> stereo)
{
    this->stereo = stereo;
}

void StereoOnCDCommand::execute() /* override */
{
    prevType = stereo->getState();
    stereo->on();
    stereo->setCD();
    stereo->setVolume(5);

}

void StereoOnCDCommand::undo() /* override */
{
    stereo->off();
    setUndo(stereo, prevType);
    
}


/* Stereo On DVD Command */
StereoOnDVDCommand::StereoOnDVDCommand(shared_ptr<Stereo> stereo)
{
    this->stereo = stereo;
}

void StereoOnDVDCommand::execute() /* override */
{
    prevType = stereo->getState();
    stereo->on();
    stereo->setDVD();
    stereo->setVolume(15);

}

void StereoOnDVDCommand::undo() /* override */
{
    stereo->off();
    setUndo(stereo, prevType);
    
}


/* Stereo On Radio Command */
StereoOnRadioCommand::StereoOnRadioCommand(shared_ptr<Stereo> stereo)
{
    this->stereo = stereo;
}

void StereoOnRadioCommand::execute() /* override */
{
    prevType = stereo->getState();
    stereo->on();
    stereo->setRadio();
    stereo->setVolume(30);

}

void StereoOnRadioCommand::undo() /* override */
{
    stereo->off();
    setUndo(stereo, prevType);
    
}


/* Stereo On Cloud Music Command */
StereoOnCloudCommand::StereoOnCloudCommand(shared_ptr<Stereo> stereo)
{
    this->stereo = stereo;
}

void StereoOnCloudCommand::execute() /* override */
{
    prevType = stereo->getState();
    stereo->on();
    stereo->setCloud();
    stereo->setVolume(50);

}

void StereoOnCloudCommand::undo() /* override */
{
    stereo->off();
    setUndo(stereo, prevType);
    
}


/* Stereo Off Command */
StereoOffCommand::StereoOffCommand(shared_ptr<Stereo> stereo)
{
    this->stereo = stereo;
}

void StereoOffCommand::execute() /* override */
{
    prevType = stereo->getState();
    stereo->off();
    stereo->setVolume(0);

}

void StereoOffCommand::undo() /* override */
{
    stereo->on();
    setUndo(stereo, prevType);
    
}