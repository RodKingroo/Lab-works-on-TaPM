/* Copyright (c) 2022 RodKingroo */
#include "Stereo.h"

void Stereo::on()
{
    cout << "Stereo On" << endl;
}

void Stereo::off()
{
    cout << "Stereo Off" << endl;
}


void Stereo::setCassette()
{
    state = CASSETTE;
    cout << "Cassette Rec Selected" << endl;
}

void Stereo::setCD()
{
    state = CD;
    cout << "CD device selected" << endl;
}

void Stereo::setDVD()
{
    state = DVD;
    cout << "DVD device selected" << endl;
}

void Stereo::setRadio()
{
    state = RADIO;
    cout << "Radio device selected" << endl;
}

void Stereo::setCloud()
{
    state = CLOUDMUSIC;
    cout << "Voice Assist play music" << endl;
}

void Stereo::setVolume(int volume)
{
    this->volume = volume;
    cout << "Volume level: " << volume << endl;
}

const int Stereo::getVolume() { return volume; }

const int Stereo::getState() { return state; }