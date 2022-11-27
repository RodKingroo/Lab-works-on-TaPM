/* Copyright (c) 2022 RodKingroo */
#include "StreetLight.h"

void StreetLight::on()
{
    cout << "Street Street Light on" << endl;
}

void StreetLight::off()
{
    cout << "Street Street Light off" << endl;
}


void StreetLight::state_1()
{
    bright = STATE_ONE;
    cout << "Bright Street Light: " << bright << endl;
}

void StreetLight::state_2()
{
    bright = STATE_TWO;
    cout << "Bright Street Light: " << bright << endl;
}

void StreetLight::state_3()
{
    bright = STATE_THREE;
    cout << "Bright Street Light: " << bright << endl;
}

void StreetLight::state_4()
{
    bright = STATE_FOUR;
    cout << "Bright Street Light: " << bright << endl;
}

void StreetLight::state_5()
{
    bright = STATE_FIVE;
    cout << "Bright Street Light: " << bright << endl;
}

const int StreetLight::getState() { return bright; }