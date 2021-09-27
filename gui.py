import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic, QtTest
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread

import weather_data
import time
import datetime

class WeatherData(QThread):
    req = weather_data.get_weather_data()
    cur_temp = req['cur_temp']
    min_temp = req['min_temp']
    max_temp = req['max_temp']
    pressure = req['pressure']
    wind_speed = req["wind_speed"]
    icon_id = req['icon_id']
    weekday = req["weekday"]
    city = req["city"]
    description = req["description"]
    sunset = req["sunset"]
    sunrise = req["sunrise"]
    humidity = req["humidity"]
    feels_like = req["feels_like"]

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        while True :
            try :
                self.req = weather_data.get_weather_data()

            except :
               self.req['cur_temp'] = self.cur_temp
               self.req["min_temp"] = self.min_temp
               self.req['max_temp'] = self.max_temp
               self.req["pressure"] = self.pressure
               self.req['wind_speed'] = self.wind_speed
               self.req['city'] = self.city
               self.req['icon_id'] = self.icon_id
               self.req["weekday"] = self.weekday
               self.req["description"] = self.description
               self.req["sunset"] = self.sunset
               self.req["sunrise"] = self.sunrise
               self.req["humidity"] = self.humidity
               self.req["feels_like"] = self.feels_like


            self.cur_temp = self.req['cur_temp']
            self.min_temp = self.req['min_temp']
            self.max_temp = self.req['max_temp']
            self.pressure = self.req['pressure']
            self.wind_speed = self.req["wind_speed"]
            self.city = self.req["city"]
            self.icon_id = self.req["icon_id"]
            self.weekday = self.req["weekday"]
            self.description = self.req['description']
            self.sunset = self.req["sunset"]
            self.sunrise = self.req["sunrise"]
            self.humidity = self.req["humidity"]
            self.feels_like = self.req["feels_like"]
            time.sleep(300)





class App(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.weather_data = WeatherData()
        self.weather_data.start()
        self.set_up()
        self.set_data()

    def set_up(self):
        self.root = uic.loadUi('new_root.ui')
        self.root.show()

    def set_data(self):
        self.root.location_l.setText(self.weather_data.city + "\n "   + self.weather_data.weekday)
        self.root.cur_temp_l.setText(str(self.weather_data.cur_temp) + '°C')
        self.root.wind_speed_l.setText(f" Ветер {str(self.weather_data.wind_speed)} м/c")
        self.root.pressure_l.setText( f" Давление {str(self.weather_data.pressure)} мбар")
        weather_cond_logo = QPixmap(f"icons/{self.weather_data.icon_id}.png").scaledToHeight(85).scaledToWidth(85)
        self.root.icon_l.setPixmap(weather_cond_logo)
        date = datetime.datetime.today()
        self.root.time_l.setText( f"Обновлено в {datetime.datetime.strftime(date , '%H:%M')}")
        self.root.description_l.setText(self.weather_data.description.capitalize())
        self.root.dawn_time_l.setText(f" Закат    {datetime.datetime.strftime(self.weather_data.sunset , '%H:%M')}")
        self.root.dust_time_l.setText(f" Рассвет    {datetime.datetime.strftime(self.weather_data.sunrise , '%H:%M')}")
        self.root.humidity_l.setText(f" Влажность {self.weather_data.humidity} %")
        self.root.feels_like_l.setText(f" Ощущ.как {self.weather_data.feels_like}°C")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
