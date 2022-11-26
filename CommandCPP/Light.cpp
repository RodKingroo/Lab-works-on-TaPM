/* Copyright (c) 2022 RodKingroo */
#include "Light.h"

void Light::on()
{
    cout << "Light on" << endl;
}

void Light::off()
{
    cout << "Light off" << endl;
}


void Light::state_1()
{
    bright = STATE_ONE;
    cout << "Bright light: " << bright << endl;
}

void Light::state_2()
{
    bright = STATE_TWO;
    cout << "Bright light: " << bright << endl;
}

void Light::state_3()
{
    bright = STATE_THREE;
    cout << "Bright light: " << bright << endl;
}

void Light::state_4()
{
    bright = STATE_FOUR;
    cout << "Bright light: " << bright << endl;
}

void Light::state_5()
{
    bright = STATE_FIVE;
    cout << "Bright light: " << bright << endl;
}

const int Light::getState() { return bright; }