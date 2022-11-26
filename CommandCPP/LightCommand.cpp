/* Copyright (c) 2022 RodKingroo */
#include "LightCommand.h"

void setUndo(shared_ptr<Light> light, int prevBright)
{
    switch (prevBright)
    {
        case Light::OFF:
            light->off();
        case Light::STATE_ONE:
            light->state_1();
            break;
        case Light::STATE_TWO:
            light->state_2();
            break;
        case Light::STATE_THREE:
            light->state_3();
            break;
        case Light::STATE_FOUR:
            light->state_4();
            break;
        case Light::STATE_FIVE:
            light->state_5();
            break;

    }
}


/* Light On State One Command */
LightOnStateOneCommand::LightOnStateOneCommand(shared_ptr<Light> light)
{
    this->light = light;
}

void LightOnStateOneCommand::execute() /* override */
{
    prevBright = light->getState();
    light->on();
    light->state_1();
}

void LightOnStateOneCommand::undo() /* override */
{
    light->off();
    setUndo(light, prevBright);
}



/* Light on State Two Command */
LightOnStateTwoCommand::LightOnStateTwoCommand(shared_ptr<Light> light)
{
    this->light = light;

}

void LightOnStateTwoCommand::execute() /* override */
{
    prevBright = light->getState();
    light->on();
    light->state_2();

}

void LightOnStateTwoCommand::undo() /* override */
{
    light->off();
    setUndo(light, prevBright);
}


/* Light on State Three Command */
LightOnStateThreeCommand::LightOnStateThreeCommand(shared_ptr<Light> light)
{
    this->light = light;
}

void LightOnStateThreeCommand::execute() /* override */
{
    prevBright = light->getState();
    light->on();
    light->state_3();

}

void LightOnStateThreeCommand::undo() /* override */
{
    light->off();
    setUndo(light, prevBright);
}


/* Light on State Three Command */
LightOnStateFourCommand::LightOnStateFourCommand(shared_ptr<Light> light)
{
    this->light = light;
}

void LightOnStateFourCommand::execute() /* override */
{
    prevBright = light->getState();
    light->on();
    light->state_4();
}

void LightOnStateFourCommand::undo() /* override */
{
    light->off();  
    setUndo(light, prevBright);
}


/* Light on State Five Command */
LightOnStateFiveCommand::LightOnStateFiveCommand(shared_ptr<Light> light)
{
    this->light = light;
}

void LightOnStateFiveCommand::execute() /* override */
{
    prevBright = light->getState();
    light->on();
    light->state_5();
}

void LightOnStateFiveCommand::undo() /* override */
{
    light->off();
    setUndo(light, prevBright);
}


/* Light on Off Command */
LightOffCommand::LightOffCommand(shared_ptr<Light> light)
{
    this->light = light;
}

void LightOffCommand::execute() /* override */
{
    prevBright = light->getState();
    light->off();
}

void LightOffCommand::undo() /* override */
{
    light->on();
    setUndo(light, prevBright);
}