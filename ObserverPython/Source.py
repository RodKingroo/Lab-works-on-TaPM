from abc import ABC, abstractmethod
from design import Ui_MainWindow
import requests

class iObserver(ABC):
    @abstractmethod
    def Update(self) : pass

class iSubject(ABC):
    @abstractmethod
    def RegisterObserver(self, observer) : pass
    @abstractmethod
    def RemoveObserver(self, observer) : pass
    @abstractmethod
    def NotifyObservers(self, observer) : pass

class iDisplayElement(ABC):
    @abstractmethod
    def Display(self) : pass

class WeatherData(iSubject):
    def __init__(self):
        self.observers = [] 
        self.temperature = 0
        self.humidity = 0
        self.min_temperature = 0
        self.max_temperature = 0
        self.pressure = 0
        self.feels_like = 0

    def RegisterObserver(self, observer):
        self.observers.append(observer)

    def RemoveObserver(self, observer):
        self.observers.remove(observer)

    def NotifyObservers(self):
        for o in self.observers:
            o.Update(self.temperature, self.humidity, self.min_temperature, self.max_temperature, self.pressure, self.feels_like)

    def measurementsChanged(self):
        self.NotifyObservers()

    def setMeasurements(self, temperature, humidity, min_temperature, max_temperature, pressure, feels_like):
        self.temperature = temperature
        self.humidity = humidity
        self.min_temperature = min_temperature
        self.max_temperature = max_temperature
        self.pressure = pressure
        self.feels_like = feels_like
        self.measurementsChanged()

class CurrentConditionsDisplay(iObserver, iDisplayElement):
    def __init__(self, weatherData, ui):
        self.weatherData = weatherData
        self.ui = ui
        weatherData.RegisterObserver(self)

    def Update(self, temperature, humidity, min_temperature, max_temperature, pressure, feels_like):
        self.temperature = temperature
        self.humidity = humidity
        self.Display()

    def Display(self):
        print ("Current conditions: " + str(self.temperature) + "'C degrees and " + str(self.humidity) + "% humidity ")
        self.ui.set_temp("Temperature: " + str(round(self.temperature - 273, 2)) + "'C or " + str(self.temperature) + "'F ")
        self.ui.set_hum("Humidity: " + str(self.humidity) + "% ")
        

    def Unregister(self):
        self.weatherData.RemoveObserver(self)

class StatisticDisplay(iObserver, iDisplayElement):
    def __init__ (self, weatherData, ui):
        self.weatherData = weatherData
        self.ui = ui
        weatherData.RegisterObserver(self)

    def Update(self, temperature, humidity, min_temperature, max_temperature, pressure, feels_like):
        self.min_temperature = min_temperature
        self.max_temperature = max_temperature
        self.Display()
        

    def Display(self):
        print("Current min temperature: " + str(self.min_temperature) + "'C; average temperature: " + str(((self.min_temperature + self.max_temperature) / 2)) + "'C Max: "  + str(self.max_temperature) +  "'C ")
        self.ui.set_min_temp("Minimal temperature: " + str(round(self.min_temperature - 273, 2)) + "'C or " + str(self.min_temperature) + "'F")
        self.ui.set_ave_temp("Average temperature: " + str(round(((self.min_temperature + self.max_temperature)/2) - 273, 2)) + "'C or " + str(round((self.min_temperature + self.max_temperature)/2, 2)) + "'F")
        self.ui.set_max_temp("Maximal temperature: " + str(round(self.max_temperature - 273, 2)) + "'C or " + str(self.max_temperature) + "'F")

    def Unregister(self):
        self.weatherData.RemoveObserver(self)

class ForecastDisplay(iObserver, iDisplayElement):
    def __init__ (self, weatherData, ui):
        self.weatherData = weatherData
        self.ui = ui
        weatherData.RegisterObserver(self)

    def Update(self, temperature, humidity, min_temperature, max_temperature, pressure, feels_like):
        self.pressare = pressure
        self.Display()
        

    def Display(self):
        print("Atmospheric pressure is " + str(self.pressare) + " millimeters of mercury")
        self.ui.set_pres("Pressure: " + str(self.pressare) + " millimeters of mercury")

    def Unregister(self):
        self.weatherData.RemoveObserver(self)

class FeelsLike(iObserver, iDisplayElement):
    def __init__ (self, weatherData, ui):
        self.weatherData = weatherData
        self.ui = ui
        weatherData.RegisterObserver(self)

    def Update(self, temperature, humidity, min_temperature, max_temperature, pressure, feels_like):
        self.temperature = temperature
        self.feels_like = feels_like
        self.Display()
        

    def Display(self):
        print("The feels like " + str(self.feels_like) + "'C")
        self.ui.set_feels("Feels like: " + str(round(self.feels_like - 273, 2)) + "'C or " + str(self.feels_like) + "'F")

    def Unregister(self):
        self.weatherData.RemoveObserver(self)


