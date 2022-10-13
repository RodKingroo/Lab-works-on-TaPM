// Copyright (c) 2022 RodKingroo

#include "Pet.h"
#include "Cat.h"
#include "Dog.h"
#include "Rabbit.h"

#include <iostream>
#include <locale.h>

using namespace std;

int main() {
	setlocale(LC_ALL, "rus");
	cout << "����� �������� �� ������?" << endl << "1. �����"
										<< endl << "2. ������"
										<< endl << "3. ������"
										<< endl << "(�������� 1-3): ";

	int choise;
	cin >> choise;

	Pet* p;
	switch (choise) {
	case 1: p = new Cat(); break;
	case 2: p = new Dog(); break;
	case 3:	p = new Rabbit(); break;
	default: cout << "��� �� �������"; return 0;
	}
	cout << "���������� ��� ������ �������: ";
	char n[100];
	cin.ignore();
	cin.getline(n, 100);

	p->setName(n);
	p->play();
	delete p;

}