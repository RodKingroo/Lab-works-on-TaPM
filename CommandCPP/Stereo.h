/* Copyright (c) 2022 RodKingroo */
#pragma once
#include <iostream>

using namespace std;

class Stereo
{
private:
    int volume = 0;
    int state = UNKNOWN;
public:
    void on();
    void off();

    void setCassette();
    void setCD();
    void setDVD();
    void setRadio();
    void setCloud();

    void setVolume(int volume);
    const int getVolume();

    const int getState();

    static enum {
        UNKNOWN = 0,
        CASSETTE = 1,
        CD = 2,
        DVD = 3,
        RADIO = 4,
        CLOUDMUSIC = 5,
    };

};