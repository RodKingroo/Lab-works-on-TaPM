// Copyright (c) 2022 RodKingroo

#include <iostream>
#include <list>

class iObserver
{
public:
	virtual void Update(float temperature, float himidity, float min_temperature, float max_temperature, float pressure, float feels_like) = 0;

};

class iDisplayElement
{
public:
	virtual void display() = 0;

};

class iSubject
{
public:
	virtual void registerObserver(iObserver& o) = 0;
	virtual void removeObserver(iObserver& o) = 0;
	virtual void notifyObservers() = 0;
};

class WeatherData : public iSubject {
private:
	std::list<iObserver*> observers;
	float temperature;
	float humidity;

	float min_temperature;
	float max_temperature;

	float pressure;

	float feels_like;

public:
	void registerObserver(iObserver& o)override {
		observers.push_back(&o);

	}

	void removeObserver(iObserver& o) override {
		observers.remove(&o);

	}

	void notifyObservers() override {
		for (auto it = observers.begin(); it != observers.end(); it++) {
			(*it)->Update(temperature, humidity, min_temperature, max_temperature, pressure, feels_like);

		}

	}

	void measurementsChanged() {
		notifyObservers();

	}

	void setMeasurements(float temperature, float humidity, float min_temperature, float max_temperature, float pressure, float feels_like) {
		this->temperature = temperature;
		this->humidity = humidity;
		this->min_temperature = min_temperature;
		this->max_temperature = max_temperature;
		this->pressure = pressure;
		this->feels_like = feels_like;
		measurementsChanged();

	}


};

class CurrentConditionsDisplay : public iObserver, iDisplayElement {
private:
	float temperature;
	float humidity;

	iSubject& weatherData;

public:
	CurrentConditionsDisplay(iSubject& weatherData) : weatherData(weatherData) {
		weatherData.registerObserver(*this);

	}

	void Update(float temperature, float humidity, float min_temperature, float max_temperature, float pressure, float feels_like) override {
		this->temperature = temperature;
		this->humidity = humidity;
		display();

	}

	void display() override {
		std::cout << "Current conditions: " << temperature-273 << "'C degrees and " << humidity << "% humidity" << std::endl;

	}

	void unregister() {
		weatherData.removeObserver(*this);

	}

};

class StatisticDisplay : public iObserver, iDisplayElement {
private:
	float min_temperature;
	float max_temperature;
	iSubject& weatherData;

public:
	StatisticDisplay(iSubject& weatherData) : weatherData(weatherData) {
		weatherData.registerObserver(*this);

	}

	void Update(float temperature, float humidity, float min_temperature, float max_temperature, float pressure, float feels_like) {
		this->min_temperature = min_temperature;
		this->max_temperature = max_temperature;
		display();

	}
	
	void display() override {
		std::cout << "Current min temperature: " << min_temperature - 273 << "'C; average temperature: " << ((min_temperature + max_temperature)/2) - 273
			<< "'C; max temperature: " << max_temperature - 273 << "'C; " << std::endl;

	}

	void unregister() {
		weatherData.removeObserver(*this);
	}

};

class ForecastDisplay : public iObserver, iDisplayElement {
private:
	float pressure;
	iSubject& weatherData;

public:
	ForecastDisplay(iSubject& weatherData) : weatherData(weatherData) {
		weatherData.registerObserver(*this);

	}

	void Update(float temperature, float humidity, float min_temperature, float max_temperature, float pressure, float feels_like) override {
		this->pressure = pressure;
		display();

	}

	void display() override {
		std::cout << "Atmospheric pressure is " << pressure << " millimeters of mercury" << std::endl;

	}

	void unregistred() {
		weatherData.removeObserver(*this);

	}

};

class FeelsLike : public iObserver, iDisplayElement {
private:
	float temperature;
	float feels_like;
	iSubject& weatherData;

public:
	FeelsLike(iSubject& weatherData) : weatherData(weatherData) {
		weatherData.registerObserver(*this);

	}

	void Update(float temperature, float humidity, float min_temperature, float max_temperature, float pressure, float feels_like) override {
		this->temperature = temperature;
		this->feels_like = feels_like;
		display();

	}

	void display() override {
		std::cout << "The actual temperature is " << temperature - 273 << "'C, feels like " << feels_like - 273 << "'C" << std::endl;

	}

	void unregistred() {
		weatherData.removeObserver(*this);

	}
};

int main() {
	WeatherData weatherData;
	CurrentConditionsDisplay currentDisplay(weatherData);
	StatisticDisplay statisticDisplay(weatherData);
	ForecastDisplay forecastDisplay(weatherData);
	FeelsLike feelsLike(weatherData);

	weatherData.setMeasurements(225, 65, 215, 315, 120.0f, 308);
	
	return 0;

}

