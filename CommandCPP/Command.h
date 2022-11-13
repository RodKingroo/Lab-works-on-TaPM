/* Copyright (c) 2022 RodKingroo */

#pragma once

class Command 
{
public:
	virtual void execute() = 0;
	virtual void undo() = 0;

};