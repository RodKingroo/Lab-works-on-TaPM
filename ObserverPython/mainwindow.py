import sys
from Source import *
from PyQt5 import QtWidgets
from design import Ui_MainWindow


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def set_temp(self, value):
        self.ui.temp.setText(value)

    def set_hum(self, value):
        self.ui.hum.setText(value)

    def set_min_temp(self, value):
        self.ui.min_t.setText(value)

    def set_ave_temp(self, value):
        self.ui.ave_t.setText(value)

    def set_max_temp(self, value):
        self.ui.max_t.setText(value)

    def set_pres(self, value):
        self.ui.pres.setText(value)

    def set_feels(self, value):
        self.ui.feels.setText(value)
        
 

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    weatherData = WeatherData()
    currentDisplay = CurrentConditionsDisplay(weatherData, application)
    statisticDisplay = StatisticDisplay(weatherData, application)
    forecastDisplay = ForecastDisplay(weatherData, application)
    feelsLike = FeelsLike(weatherData, application)

    
    s_city = "Omsk"
    appid = "a34ec4c11abb184e69957e9d6686ba03"
    res = requests.get("http://api.openweathermap.org/data/2.5/find?q=" + s_city + "&type=like&APPID=" + appid)
    data = res.json()


    temp = data['list'][0]['main']['temp']
    humidity = data['list'][0]['main']['humidity']

    temp_min = data['list'][0]['main']['temp_min']
    temp_max = data['list'][0]['main']['temp_max']
    
    pressure = data['list'][0]['main']['pressure']

    feels_like = data['list'][0]['main']['feels_like']
   
    weatherData.setMeasurements(temp, humidity, temp_min, temp_max, pressure, feels_like)

sys.exit(app.exec())