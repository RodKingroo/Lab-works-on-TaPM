#include "enums_class.h"

#include <iostream>
#include <list>

class Pizza 
{
protected:
	NYPizzaName _nyPizzaName;
	ChicagoPizzaName _chicagoPizzaName; std::string name;
	Dough _dough;						std::string dough;
	Sauce _sauce;						std::string sauce;
	Time _time;							std::string time;
	Deegree _degree;					std::string degree;
	Ingredients _ingredients;			std::list<std::string> toppings;

public:
	virtual void prepare() 
	{
		std::cout << name << " is being prepared" << std::endl;
		std::cout << dough << " is made" << std::endl;

		if (sauce != "None") std::cout << sauce << " is added" << std::endl;
		else;
		
		for (auto t : toppings) std::cout << "Adding " << t << std::endl;

	}

	virtual void bake() 
	{
		std::cout << "Bake for " << time << " at "<< degree <<" deegree" << std::endl;
	}

	virtual void cut() 
	{
		std::cout << "Cuttings the pizza into diagonal slices" << std::endl;
	}

	virtual void box() 
	{
		std::cout << "Place pizza in official box" << std::endl;

	}

	std::string getName() { return name; }

};

class NYStyleCheesePizza : public Pizza 
{
public:
	NYStyleCheesePizza() 
	{
		name = _nyPizzaName.Cheese;
		dough = _dough.Thin;
		sauce = _sauce.Marinara;
		degree = _degree.Strong_Fire;
		time = _time.Very_Fast;
		toppings.push_back(_ingredients.Reggiano);
		toppings.push_back(_ingredients.Mozzarella);
		toppings.push_back(_ingredients.Reggiano);
		
	}

	void box() override
	{
		std::cout << "Wrap in plastic wrap" << std::endl;

	}

};

class NYStyleCarbonaraPizza : public Pizza
{
public:
	NYStyleCarbonaraPizza()
	{
		name = _nyPizzaName.Carbonara;
		dough = _dough.Thick;
		sauce = _sauce.Alfredo;
		degree = _degree.Medium_Fire;
		time = _time.Slow;
		toppings.push_back(_ingredients.Cheder);
		toppings.push_back(_ingredients.Parmezan);
		toppings.push_back(_ingredients.Tomato);
		toppings.push_back(_ingredients.Mozzarella);

	}
};

class NYStyleChorizoPizza : public Pizza
{
public:
	NYStyleChorizoPizza()
	{
		name = _nyPizzaName.Chorizo;
		dough = _dough.Basic;
		sauce = _sauce.Tomato;
		degree = _degree.Low_Fire;
		time = _time.Very_Slow;
		toppings.push_back(_ingredients.Mozzarella);
		toppings.push_back(_ingredients.Red_Pepper);
		toppings.push_back(_ingredients.Chorizo);

	}
};

class NYStyleClamPizza : public Pizza
{
public:
	NYStyleClamPizza()
	{
		name = _nyPizzaName.Clam;
		dough = _dough.Basic;
		sauce = _sauce.Lemon;
		degree = _degree.Low_Fire;
		time = _time.Very_Slow;
		toppings.push_back(_ingredients.Parmezan);
		toppings.push_back(_ingredients.Clams);
		toppings.push_back(_ingredients.Romano);
		toppings.push_back(_ingredients.Red_Pepper);

	}
};

class NYStylePepperoniPizza : public Pizza
{
public:
	NYStylePepperoniPizza()
	{
		name = _nyPizzaName.Pepperoni;
		dough = _dough.Thin;
		sauce = _sauce.Tomato;
		degree = _degree.Medium_Fire;
		time = _time.Medium;
		toppings.push_back(_ingredients.Mozzarella);
		toppings.push_back(_ingredients.Pepperoni);

	}
};

class NYStyleViggiePizza : public Pizza
{
public:
	NYStyleViggiePizza()
	{
		name = _nyPizzaName.Viggle;
		dough = _dough.Thick;
		sauce = _sauce.NoneSauce;
		degree = _degree.Medium_Fire;
		time = _time.Very_Slow;
		toppings.push_back(_ingredients.Parmezan);
		toppings.push_back(_ingredients.Tomato);
		toppings.push_back(_ingredients.Egg); 
		toppings.push_back(_ingredients.Red_Pepper);
		toppings.push_back(_ingredients.Spinate);

	}

	void box() override 
	{
		std::cout << "Wrap in foil" << std::endl;

	}
};

class ChicagoStyleCheesePizza : public Pizza
{
public:
	ChicagoStyleCheesePizza()
	{
		name = _chicagoPizzaName.Cheese;
		dough = _dough.Extra_Trick;
		sauce = _sauce.Tomato;
		degree = _degree.Medium_Fire;
		time = _time.Medium;
		toppings.push_back(_ingredients.Mozzarella);
		toppings.push_back(_ingredients.Adyghe);
		toppings.push_back(_ingredients.Reggiano);

	}

	void cut() override
	{
		std::cout << "Cutting the pizza into square slides" << std::endl;

	}

};

class ChicagoStyleCarbonaraPizza : public Pizza
{
public:
	ChicagoStyleCarbonaraPizza()
	{
		name = _chicagoPizzaName.Carbonara;
		dough = _dough.Super_Thin;
		sauce = _sauce.Alfredo;
		degree = _degree.Medium_Fire;
		time = _time.Fast;
		toppings.push_back(_ingredients.Cheder);
		toppings.push_back(_ingredients.Adyghe);
		toppings.push_back(_ingredients.Tomato);
		toppings.push_back(_ingredients.Red_Pepper);

	}

	void box() override 
	{
		std::cout << "Wrap in foil" << std::endl;

	}

	void cut() override
	{
		std::cout << "Cutting the pizza into triangular slides" << std::endl;

	}

};

class ChicagoStyleChorizoPizza : public Pizza
{
public:
	ChicagoStyleChorizoPizza() 
	{
		name = _chicagoPizzaName.Chorizo;
		dough = _dough.Thick;
		sauce = _sauce.Fat;
		degree = _degree.Medium_Fire;
		time = _time.Slow;
		toppings.push_back(_ingredients.Mozzarella);
		toppings.push_back(_ingredients.Tomato);
		toppings.push_back(_ingredients.Chorizo);

	}
};

class ChicagoStyleClamPizza : public Pizza
{
public:
	ChicagoStyleClamPizza() 
	{
		name = _chicagoPizzaName.Clam;
		dough = _dough.Basic;
		sauce = _sauce.Lemon;
		degree = _degree.Medium_Fire;
		time = _time.Very_Slow;
		toppings.push_back(_ingredients.Parmezan);
		toppings.push_back(_ingredients.Clams);
		toppings.push_back(_ingredients.Cheder);
		toppings.push_back(_ingredients.Red_Pepper);

	}
};

class ChicagoStylePepperoniPizza : public Pizza
{
public:
	ChicagoStylePepperoniPizza()
	{
		name = _chicagoPizzaName.Pepperoni;
		dough = _dough.Super_Thin;
		sauce = _sauce.Tomato;
		degree = _degree.Medium_Fire;
		time = _time.Fast;
		toppings.push_back(_ingredients.Mozzarella);
		toppings.push_back(_ingredients.Pepperoni);
		toppings.push_back(_ingredients.Cheder);
	}
};

class ChicagoStyleViggiePizza : public Pizza
{
public:
	ChicagoStyleViggiePizza() 
	{
		name = _chicagoPizzaName.Viggle;
		dough = _dough.Extra_Trick;
		sauce = _sauce.Milk;
		degree = _degree.Medium_Fire;
		time = _time.Medium;
		toppings.push_back(_ingredients.Parmezan);
		toppings.push_back(_ingredients.Tomato);
		toppings.push_back(_ingredients.Spinate);

	}
};

class PizzaStore 
{
public:
	std::shared_ptr<Pizza> orderPizza(const int& type)
	{
		std::shared_ptr<Pizza> pizza = nullptr;
		pizza = createPizza(type);
		if(pizza)
		{
			pizza->prepare();
			pizza->bake();
			pizza->cut();
			pizza->box();
			return pizza;

		}
		else 
		{
			return nullptr;
		}
	}

	virtual std::shared_ptr<Pizza> createPizza(const int& type) = 0;
};

class NYPizzaStore : public PizzaStore
{
	std::shared_ptr<Pizza> createPizza(const int& type) override
	{
		switch (type)
		{
		case cheese:
			return std::make_shared<NYStyleCheesePizza>();
			break;
		case pepperoni:
			return std::make_shared<NYStylePepperoniPizza>();
			break;
		case carbonara:
			return std::make_shared<NYStyleCarbonaraPizza>();
			break;
		case chorizo:
			return std::make_shared<NYStyleChorizoPizza>();
			break;
		case clam:
			return std::make_shared<NYStyleClamPizza>();
			break;
		case viggle:
			return std::make_shared<NYStyleViggiePizza>();
			break;
		default:
			return nullptr;
			break;
		}
	}
};

class ChicagoPizzaStore : public PizzaStore 
{
	
	std::shared_ptr<Pizza>createPizza(const int& type) override {
		switch (type)
		{
		case cheese:
			return std::make_shared<ChicagoStyleCheesePizza>();
			break;
		case pepperoni:
			return std::make_shared<ChicagoStylePepperoniPizza>();
			break;
		case carbonara:
			return std::make_shared<ChicagoStyleCarbonaraPizza>();
			break;
		case chorizo:
			return std::make_shared<ChicagoStyleChorizoPizza>();
			break;
		case clam:
			return std::make_shared<ChicagoStyleClamPizza>();
			break;
		case viggle:
			return std::make_shared<ChicagoStyleViggiePizza>();
			break;
		default:
			return nullptr;
			break;
		}
	}
};

int main() 
 {
	int style = NewYork, name = carbonara;
	std::unique_ptr<PizzaStore> Store;

	if (style == NewYork) Store = std::make_unique<NYPizzaStore>();
	else if (style == Chicago) Store = std::make_unique<ChicagoPizzaStore>();

	std::shared_ptr<Pizza> pizza = Store->orderPizza(name);
	if (pizza) std::cout << "Your pizza " << pizza->getName() << std::endl;
	else std::cout << "We are so sorry" << std::endl;

	return 0;
}