// Copyright (c) 2022 RodKingroo

#include "Source.h"
#include "enums_class.h"

#include <iostream>
#include <list>

class Pizza
{
public: 
	PizzaName pn;	std::string name;
	Dough d;		std::string dough;
	Sauce s;		std::string sauce;
	Time t;			std::string time;
	Deegree dgr;	std::string degree;
	Ingredients i;  std::list<std::string> toppings;

	void prepare()
	{
		std::cout << "Preparing: " << name << std::endl;
		std::cout << "Tossing: " << dough << std::endl;
		std::cout << "Adding sauce: " << sauce << std::endl;
		std::cout << "Adding toppings: " << std::endl;
		for (auto t : toppings) std::cout << "\t - " << t << std::endl;

	}

	void bake()
	{
		std::cout << "Bake for " << time << " at " << degree << std::endl;

	}

	void cut()
	{
		std::cout << "Cutting the pizza into diagonal slices " << std::endl;

	}

	void box()
	{
		std::cout << "Place pizza in official box " << std::endl;

	}

	std::string getName() { return name; }

};

class CheesePizza : public Pizza
{
public:
	CheesePizza()
	{
		name = pn.Cheese;
		dough = d.Basic;
		sauce = s.Fat;
		time = t.fast;
		degree = dgr.Five_hundred;
		toppings.push_back(i.mozarella);
		toppings.push_back(i.parmezan);
		toppings.push_back(i.mozarella);

	}

};

class PeperoniPizza : public Pizza
{
public:
	PeperoniPizza()
	{
		name = pn.Pepperoni;
		dough = d.Thin;
		sauce = s.Tomat;
		time = t.medium;
		degree = dgr.Four_plusHalf_hundred;
		toppings.push_back(i.mozarella);
		toppings.push_back(i.pepperoni);

	}

};

class ClamPizza : public Pizza {
public:
	ClamPizza() 
	{
		name = pn.Clam;
		dough = d.Basic;
		sauce = s.Lemon;
		time = t.slow;
		degree = dgr.Four_plusHalf_hundred;
		toppings.push_back(i.parmezan);
		toppings.push_back(i.clams);
		toppings.push_back(i.romano);
		toppings.push_back(i.red);

	}
};

class VigglePizza : public Pizza 
{
public:
	VigglePizza() 
	{
		name = pn.Viggle;
		dough = d.Basic;
		sauce = s.NoneSauce;
		time = t.very_slow;
		degree = dgr.Three_Seventeen_five_Hunded;
		toppings.push_back(i.parmezan);
		toppings.push_back(i.tomato);
		toppings.push_back(i.egg);
		toppings.push_back(i.red);
		toppings.push_back(i.spinate);

	}
};

class SimplePizzaFactory
{
public:

	Pizza* createPizza(int type)
	{
		Pizza* pizza = nullptr;
		switch (type)
		{
		case cheese:
			pizza = new CheesePizza();
			break;
		case pepperoni:
			pizza = new PeperoniPizza();
			break;
		case clam:
			pizza = new ClamPizza();
			break;
		case viggle:
			pizza = new VigglePizza();
			break;
		default:
			return pizza;
			break;
		}
		

	}

};

class PizzaStore
{
	SimplePizzaFactory& factory;
public:
	PizzaStore(SimplePizzaFactory& factory) : factory(factory)
	{

	}

	Pizza* orderPizza(int type)
	{
		Pizza* pizza = nullptr;
		pizza = factory.createPizza(type);
		pizza->prepare();
		pizza->bake();
		pizza->cut();
		pizza->box();
		return pizza;

	}

};

int main()
{
	SimplePizzaFactory pizzaFactory;
	PizzaStore pizzaStore(pizzaFactory);
	Pizza* p = pizzaStore.orderPizza(clam);
	std::cout << "Your pizza: " << p->getName() << std::endl;
	delete p;
	return 0;

}


