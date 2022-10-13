// Copyright (c) 2022 RodKingroo

#pragma once
#define _CRT_SECURE_NO_WARNINGS 1
#include "Pet.h"
#include <cstring>
#include <iostream>

using namespace std;

class Cat :public Pet {
private:
	char* name;
public:
	char* getName() const override {
		return this->name;
	}
	void setName(const char* name) override {
		this->name = new char[strlen(name) + 1];
		strcpy(this->name, name);
	}

	void play() override {
		cout << name << " ����� ������ � �������� �������" << endl;
	}
	~Cat() {
		if (name) delete[] name;

	}
};



