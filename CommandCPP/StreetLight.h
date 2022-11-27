/* Copyright (c) 2022 RodKingroo */
#pragma once
#include <iostream>

using namespace std;

class StreetLight
{
private:
    int bright = OFF;
public:
    void on();
    void off();
    
    void state_1();
    void state_2();
    void state_3();
    void state_4();
    void state_5();

    const int getState();

    static enum {
        OFF = 0,
        STATE_ONE = 20,
        STATE_TWO = 40,
        STATE_THREE = 60,
        STATE_FOUR = 80,
        STATE_FIVE = 100,
    };
};