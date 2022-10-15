#include <iostream>
#include <list>

class Pizza 
{
protected:
	std::string name;
	std::string dough;
	std::string sauce;
	std::list<std::string> toppings;

public:
	virtual void prepare() 
	{
		std::cout << "Preparing " << name << std::endl;
		std::cout << "Tossing " << dough << "..." << std::endl;
		std::cout << "Adding " << sauce << "..." << std::endl;
		std::cout << "Adding toppings: " << std::endl;
		for (auto t : toppings) std::cout << "\t -" << "t" << std::endl;

	}

	virtual void bake() 
	{
		std::cout << "Bake for 25 min at 350 deegree" << std::endl;
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
		name = "NY Style Sauce and Cheese Pizza";
		dough = "Thin Crust Dough";
		sauce = "Marinara Sauce";
		toppings.push_back("Grated Reggiano Cheese");

	}
};

class ChicagoStyleCheesePizza : public Pizza 
{
public:
	ChicagoStyleCheesePizza() 
	{
		name = "Chicago Style Deep Dish Cheese Pizza";
		dough = "Extra Thick Crush Dough";
		sauce = "Plum Tomato Sauce";
		toppings.push_back("Shradded Mozzarella Cheese");

	}

	void cut() override 
	{
		std::cout << "Cutting the pizza into square slides" << std::endl;

	}
};

class PizzaStore 
{
public:
	std::shared_ptr<Pizza> orderPizza(const std::string& type)
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

	virtual std::shared_ptr<Pizza> createPizza(const std::string& type) = 0;
};

class NYPizzaStore : public PizzaStore
{
	std::shared_ptr<Pizza> createPizza(const std::string& type) override
	{
		if (type == "cheese") 
		{
			return std::make_shared<NYStyleCheesePizza>();

		}
		else
		{
			std::cout << "Have no this pizza type yet" << std::endl;
			return nullptr;
		}
	}
};

class ChicagoPizzaStore : public PizzaStore 
{
	std::shared_ptr<Pizza>createPizza(const std::string& type) override {
		if (type == "cheese") 
		{
			return std::make_shared<ChicagoStyleCheesePizza>();
		}
		else 
		{
			std::cout << "Have no this  type yet" << std::endl;
			return nullptr;
		}
	}
};

int main() 
 {
	std::unique_ptr<PizzaStore> nyStore = std::make_unique<NYPizzaStore>();
	std::unique_ptr<PizzaStore> chicagoStore = std::make_unique<ChicagoPizzaStore>();
	std::shared_ptr<Pizza> pizza = nyStore->orderPizza("cheese");
	if (pizza)
		std::cout << "Your pizza " << pizza->getName() << std::endl;
	else 
		std::cout << "We are so sorry" << std::endl;
	std::cout << std::endl;
	pizza = chicagoStore->orderPizza("cheese");
	if (pizza)
		std::cout << "Your pizza " << pizza->getName() << std::endl;
	else
		std::cout << "We are so sorry" << std::endl;
	std::cout << std::endl;
	pizza = chicagoStore->orderPizza("pepperoni");
	if (pizza)
		std::cout << "Your pizza " << pizza->getName() << std::endl;
	else
		std::cout << "We are so sorry" << std::endl;

	return 0;
}