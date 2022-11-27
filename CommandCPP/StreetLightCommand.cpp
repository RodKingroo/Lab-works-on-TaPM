/* Copyright (c) 2022 RodKingroo */
#include "StreetLightCommand.h"

void setUndo(shared_ptr<StreetLight> light, int prevBright)
{
    switch (prevBright)
    {
        case StreetLight::OFF:
            light->off();
            break;
        case StreetLight::STATE_ONE:
            light->state_1();
            break;
        case StreetLight::STATE_TWO:
            light->state_2();
            break;
        case StreetLight::STATE_THREE:
            light->state_3();
            break;
        case StreetLight::STATE_FOUR:
            light->state_4();
            break;
        case StreetLight::STATE_FIVE:
            light->state_5();
            break;

    }
}


/* Street Light On State One Command */
StreetLightOnStateOneCommand::StreetLightOnStateOneCommand(shared_ptr<StreetLight> light)
{
    this->light = light;
}

void StreetLightOnStateOneCommand::execute() /* override */
{
    prevBright = light->getState();
    light->on();
    light->state_1();
}

void StreetLightOnStateOneCommand::undo() /* override */
{
    light->off();
    setUndo(light, prevBright);
}



/* Street Light on State Two Command */
StreetLightOnStateTwoCommand::StreetLightOnStateTwoCommand(shared_ptr<StreetLight> light)
{
    this->light = light;

}

void StreetLightOnStateTwoCommand::execute() /* override */
{
    prevBright = light->getState();
    light->on();
    light->state_2();

}

void StreetLightOnStateTwoCommand::undo() /* override */
{
    light->off();
    setUndo(light, prevBright);
}


/* Street Light on State Three Command */
StreetLightOnStateThreeCommand::StreetLightOnStateThreeCommand(shared_ptr<StreetLight> light)
{
    this->light = light;
}

void StreetLightOnStateThreeCommand::execute() /* override */
{
    prevBright = light->getState();
    light->on();
    light->state_3();

}

void StreetLightOnStateThreeCommand::undo() /* override */
{
    light->off();
    setUndo(light, prevBright);
}


/* Street Light on State Three Command */
StreetLightOnStateFourCommand::StreetLightOnStateFourCommand(shared_ptr<StreetLight> light)
{
    this->light = light;
}

void StreetLightOnStateFourCommand::execute() /* override */
{
    prevBright = light->getState();
    light->on();
    light->state_4();
}

void StreetLightOnStateFourCommand::undo() /* override */
{
    light->off();  
    setUndo(light, prevBright);
}


/* Street Light on State Five Command */
StreetLightOnStateFiveCommand::StreetLightOnStateFiveCommand(shared_ptr<StreetLight> light)
{
    this->light = light;
}

void StreetLightOnStateFiveCommand::execute() /* override */
{
    prevBright = light->getState();
    light->on();
    light->state_5();
}

void StreetLightOnStateFiveCommand::undo() /* override */
{
    light->off();
    setUndo(light, prevBright);
}


/* Street Light on Off Command */
StreetLightOffCommand::StreetLightOffCommand(shared_ptr<StreetLight> light)
{
    this->light = light;
}

void StreetLightOffCommand::execute() /* override */
{
    prevBright = light->getState();
    light->off();
}

void StreetLightOffCommand::undo() /* override */
{
    light->on();
    setUndo(light, prevBright);
}