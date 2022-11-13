/* Copyright (c) 2022 RodKingroo */
#include "LightCommand.h"

/* Light on in hallway */
LightOnInHallway::LightOnInHallway(shared_ptr<Light> light)
{
    this->light = light;
}

void LightOnInHallway::execute()
{
    light->on();
    light->setHallway();
}

void LightOnInHallway::undo()
{
    light->off();

}


/* Light on in Livinroom */
LightOnInLivinroom::LightOnInLivinroom(shared_ptr<Light> light)
{
    this->light = light;
}

void LightOnInLivinroom::execute()
{
    light->on();
    light->setHallway();
}

void LightOnInLivinroom::undo()
{
    light->off();

}


/* Light on in Bedroom */
LightOnInBedroom::LightOnInBedroom(shared_ptr<Light> light)
{
    this->light = light;
}

void LightOnInBedroom::execute()
{
    light->on();
    light->setHallway();
}

void LightOnInBedroom::undo()
{
    light->off();

}


/* Light on in Kitchen */
LightOnInKitchen::LightOnInKitchen(shared_ptr<Light> light)
{
    this->light = light;
}

void LightOnInKitchen::execute()
{
    light->on();
    light->setHallway();
}

void LightOnInKitchen::undo()
{
    light->off();

}


/* Light on in BathRoom */
LightOnInBathRoom::LightOnInBathRoom(shared_ptr<Light> light)
{
    this->light = light;
}

void LightOnInBathRoom::execute()
{
    light->on();
    light->setHallway();
}

void LightOnInBathRoom::undo()
{
    light->off();

}


/* Light on in StoreRoom */
LightOnInStoreRoom::LightOnInStoreRoom(shared_ptr<Light> light)
{
    this->light = light;
}

void LightOnInStoreRoom::execute()
{
    light->on();
    light->setHallway();
}

void LightOnInStoreRoom::undo()
{
    light->off();

}


/* Light on in Garage */
LightOnInGarage::LightOnInGarage(shared_ptr<Light> light)
{
    this->light = light;
}

void LightOnInGarage::execute()
{
    light->on();
    light->setHallway();
}

void LightOnInGarage::undo()
{
    light->off();

}