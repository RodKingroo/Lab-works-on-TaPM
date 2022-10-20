# Copyright (c) 2022 RodKingroo
import enum

class PizzaEnum (enum.Enum):
    cheese = "1"
    pepperoni = "2"
    clam = "3"
    viggie = "4"
    chorizo = "5"
    carbonara = "6"

class Ingredients:
    Reggiano = "Reggiano Cheese"
    Mozarella = "Mozzarela Cheese"
    Parmezan = "Parmesan cheese"
    Cheder = "Cheder cheese"
    Romano = "Romano cheese"
    Adyghe = "Adyghe cheese"
    Dutch = "Dutch cheese"
    Pepperoni = "Pepperoni slices"
    Salami = "Salami"
    Red_Pepper = "Red pepper"
    Clams = "Chopper raw clams"
    Spinate = "Baby spinach"
    Egg = "Egg"
    Tomato = "Tomatoes"
    Chorizo = "Hot chorizo"

class NYPizzaName:
    Cheese = "NY Style Cheese Pizza"
    Pepperoni = "NY Style Pepperoni Pizza"
    Clam = "NY Style Clam Pizza"
    Viggie = "NY Style Viggie Pizza"
    Chorizo = "NY Style Chorizo Pizza"
    Carbonara = "NY Style Carbonara Pizza"

class ChicagoPizzaName:
    Cheese = "Chicago Style Cheese Pizza"
    Pepperoni = "Chicago Style Pepperoni Pizza"
    Clam = "Chicago Style Clam Pizza"
    Viggie = "Chicago Style Viggie Pizza"
    Chorizo = "Chicago Style Chorizo Pizza"
    Carbonara = "Chicago Style Carbonara Pizza"


class Dough:
    Super_Thin = "Super Thin crust dough"
    Thin = "Thin crust dough"
    Basic = "Dough of standard thickness"
    Thick = "Trick crust dough"
    Extra_Thick = "Extra Thick Crust Dough"


class Sauce:
    NoneSauce = "None"
    Marinara = "Marinara sauce"
    Tomato = "Tomato Sauce"
    Vegetarian = "Vegetarian sauce"
    Fat = "Fat-free sauce"
    Alfredo = "Special Sauce Algredo"
    Lemon = "Lemon Sauce"
    Milk = "Milk Sauce"
    Garlic = "Garlic sauce"

class Time:
    Very_Fast = "5 minute"
    Fast = "10 minute"
    Medium = "15 minute"
    Slow = "20 minute"
    Very_Slow = "25 minute"

class Degree:
    Strong_Fire = "500 deegree"
    Medium_Fire = "400 deegree"
    Low_Fire = "300 deegree"