# Copyright (c) 2022 RodKingroo
import enum

class PizzaEnum (enum.Enum):
    cheese = "1"
    pepperoni = "2"
    clam = "3"
    viggie = "4"
    chorizo = "5"
    carbonara = "6"

class IngredientsEnum:
    Reggiano = "Reggiano Cheese"
    Mozarella = "Mozzarela Cheese"
    Parmezan = "Parmesan cheese"
    Cheder = "Cheder cheese"
    Romano = "Romano cheese"
    Pepperoni = "Pepperoni slices"
    Red_Pepper = "Red pepper"
    Clams = "Chopper raw clams"
    Spinate = "Baby spinach"
    Egg = "Egg"
    Tomato = "Tomatoes"
    Chorizo = "Hot chorizo"

class NYPizzaNameEnum:
    Cheese = "NY Style Cheese Pizza"
    Pepperoni = "NY Style Pepperoni Pizza"
    Clam = "NY Style Clam Pizza"
    Viggie = "NY Style Viggie Pizza"
    Chorizo = "NY Style Chorizo Pizza"
    Carbonara = "NY Style Carbonara Pizza"

class ChicagoPizzaNameEnum:
    Cheese = "Chicago Style Cheese Pizza"
    Pepperoni = "Chicago Style Pepperoni Pizza"
    Clam = "Chicago Style Clam Pizza"
    Viggie = "Chicago Style Viggie Pizza"
    Chorizo = "Chicago Style Chorizo Pizza"
    Carbonara = "Chicago Style Carbonara Pizza"


class DoughEnum:
    Super_Thin = "Super Thin crust dough"
    Thin = "Thin crust dough"
    Basic = "Dough of standard thickness"
    Thick = "Trick crust dough"
    Extra_Thick = "Extra Thick Crust Dough"


class SauceEnum:
    NoneSauce = "None"
    Marinara = "Marinara sauce"
    Tomato = "Plum Tomato Sauce"
    

class TimeEnum:
    fast = "8 minute"
    medium = "11 minute"
    slow = "20 minute"
    very_slow = "25 minute"

class DegreeEnum:
    Five_hundred = "500 deegree"
    Four_plusHalf_hundred = "450 deegree"
    Three_Seventeen_five_Hunded = "375 deegree"