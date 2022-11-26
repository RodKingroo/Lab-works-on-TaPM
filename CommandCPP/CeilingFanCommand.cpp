#include "CeilingFanCommand.h"

void setUndo(shared_ptr<CeilingFan> ceilingFan, int prevSpeed)
{
    switch (prevSpeed)
    {
    case CeilingFan::OFF:
        ceilingFan->off();
        break;
    case CeilingFan::STATE_ONE:
        ceilingFan->state_1();
        break;
    case CeilingFan::STATE_TWO:
        ceilingFan->state_2();
        break;
    case CeilingFan::STATE_THREE:
        ceilingFan->state_3();
        break;
    case CeilingFan::STATE_FOUR:
        ceilingFan->state_4();
        break;
    case CeilingFan::STATE_FIVE:
        ceilingFan->state_5();
        break;

    }
}


/* Ceiling Fan One State Command */
CeilingFanOneStateCommand::CeilingFanOneStateCommand(shared_ptr<CeilingFan> ceilingFan)
{
    this->ceilingFan = ceilingFan;
}

void CeilingFanOneStateCommand::execute() /* override */
{
    prevSpeed = ceilingFan->getState(); /// CeilingFan.h
    ceilingFan->on(); 
    ceilingFan->state_1();

}

void CeilingFanOneStateCommand::undo() /* override */
{
    ceilingFan->off(); /// CeilingFan.h
    setUndo(ceilingFan, prevSpeed);
}


/* Ceiling Fan Two State Command */
CeilingFanTwoStateCommand::CeilingFanTwoStateCommand(shared_ptr<CeilingFan> ceilingFan)
{
    this->ceilingFan = ceilingFan;
}

void CeilingFanTwoStateCommand::execute() /* override */
{
    prevSpeed = ceilingFan->getState(); // CeilingFan.h
    ceilingFan->on();
    ceilingFan->state_2();

}

void CeilingFanTwoStateCommand::undo() /* override */
{
    ceilingFan->off(); //CeilingFan.h
    setUndo(ceilingFan, prevSpeed);
}


/* Ceiling Fan Three State Command */
CeilingFanThreeStateCommand::CeilingFanThreeStateCommand(shared_ptr<CeilingFan> ceilingFan)
{
    this->ceilingFan = ceilingFan;    
}

void CeilingFanThreeStateCommand::execute() /* override */
{
    prevSpeed = ceilingFan->getState();
    ceilingFan->on();
    ceilingFan->state_3();

}

void CeilingFanThreeStateCommand::undo() /* override */
{
    ceilingFan->off();
    setUndo(ceilingFan, prevSpeed);

}


/* Ceiling Fan Four State Command */
CeilingFanFourStateCommand::CeilingFanFourStateCommand(shared_ptr<CeilingFan> ceilingFan)
{
    this->ceilingFan = ceilingFan;

}

void CeilingFanFourStateCommand::execute() /* override */
{
    prevSpeed = ceilingFan->getState();
    ceilingFan->on();
    ceilingFan->state_4();

}

void CeilingFanFourStateCommand::undo() /* override */
{
    ceilingFan->off();
    setUndo(ceilingFan, prevSpeed);
}


/*Ceiling Fan Five State Command*/
CeilingFanFiveStateCommand::CeilingFanFiveStateCommand(shared_ptr<CeilingFan> ceilingFan)
{
    this->ceilingFan = ceilingFan;

}

void CeilingFanFiveStateCommand::execute() /* override */
{
    prevSpeed = ceilingFan->getState();
    ceilingFan->on();
    ceilingFan->state_5();

}

void CeilingFanFiveStateCommand::undo() /* override */
{
    ceilingFan->off();
    setUndo(ceilingFan, prevSpeed);

}


/* Ceiling Fan Off Command*/
CeilingFanOffCommand::CeilingFanOffCommand(shared_ptr<CeilingFan> ceilingFan)
{
    this->ceilingFan = ceilingFan;
}

void CeilingFanOffCommand::execute() /* override */
{
    prevSpeed = ceilingFan->getState();
    ceilingFan->off();

}

void CeilingFanOffCommand::undo() /* override */
{
    ceilingFan->on();
    setUndo(ceilingFan, prevSpeed);
}
