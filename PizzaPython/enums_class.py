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
    mozarella = "Mozzarela cheese"
    parmezan = "Parmesan cheese"
    cheder = "Cheder cheese"
    romano = "Romano cheese"
    pepperoni = "Pepperoni slices"
    red = "Red pepper"
    clams = "Chopper raw clams"
    spinate = "Baby spinach"
    egg = "Egg"
    tomato = "Tomatoes"
    chorizo = "Hot chorizo"


class PizzaNameEnum:
    Cheese = "Cheese Pizza"
    Pepperoni = "Pepperoni Pizza"
    Clam = "Clam Pizza"
    Viggie = "Viggie Pizza"
    Chorizo = "Chorizo Pizza"
    Carbonara = "Carbonara Pizza"

class DoughEnum:
    Basic = "Basic pizza dough"
    Thin = "Thin pizza dough"


class SauceEnum:
    NoneSauce = "None"
    Lemon = "Lemon"
    Fat = "Fat-free sauce"
    Tomat = "Tomato-and-basis pasta sauce"
    Alfredo = "Special Sauce Alfredo"


class TimeEnum:
    fast = "8 minute"
    medium = "11 minute"
    slow = "20 minute"
    very_slow = "25 minute"

class DegreeEnum:
    Five_hundred = "500 deegree"
    Four_plusHalf_hundred = "450 deegree"
    Three_Seventeen_five_Hunded = "375 deegree"