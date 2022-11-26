#include "CeilingFan.h"


void CeilingFan::on() { cout << "Ceiling Fan On " << endl; }
void CeilingFan::off() { cout << "Ceiling Fan Off " << endl; }


void CeilingFan::state_1()
{
	speed = STATE_ONE;
	cout << "Ceiling Fan Speed: " << speed << endl;
}

void CeilingFan::state_2()
{
	speed = STATE_TWO;
	cout << "Ceiling Fan Speed: " << speed << endl;

}

void CeilingFan::state_3()
{
	speed = STATE_THREE;
	cout << "Ceiling Fan Speed: " << speed << endl;
	
}

void CeilingFan::state_4()
{
	speed = STATE_FOUR;
	cout << "Ceiling Fan Speed: " << speed << endl;
	
}

void CeilingFan::state_5()
{
	speed = STATE_FIVE;
	cout << "Ceiling Fan Speed: " << speed << endl;
	
}

const int CeilingFan::getState()
{
    return speed;

}