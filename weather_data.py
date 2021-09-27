import requests
import geocoder
import datetime

API_KEY = '0c104355e3de57c712b7c5c00f219037'
HOST = 'https://api.openweathermap.org/data/2.5/'


def get_weather_data():
    g = geocoder.ip("me")
    city = g.city
    lat = g.lat
    lon  = g.lng

    req = requests.get(f"{HOST}weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=ru").json()
    print(req)
    weekdays = { '0' : 'Понедельник' ,
                 '1' : 'Вторник' ,
                 '2' : 'Среда' ,
                 '3' : 'Четверг' ,
                 '4' : 'Пятница' ,
                 '5' : 'Cуббота' ,
                 '6' : 'Воскресенье' ,
                 }
    return  {
        "city" : req['name'],
        "cur_temp" : req['main']["temp"],
        "min_temp" : req['main']["temp_min"] ,
        "max_temp" : req['main']['temp_max'] ,
        "wind_speed" : req['wind']['speed'] ,
        "pressure" : req['main']["pressure"] ,
        "icon_id" : req['weather'][0]['icon'] ,
        "weekday" : weekdays[str(datetime.datetime.today().weekday())] ,
        "description" : req["weather"][0]['description'] ,
        "sunrise" : datetime.datetime.fromtimestamp(req["sys"]["sunrise"]),
        "sunset" : datetime.datetime.fromtimestamp(req["sys"]["sunset"]) ,
        "humidity" : req["main"]["humidity"] ,
        "feels_like" : req["main"]["feels_like"]

    }
if __name__ == '__main__':
   get_weather_data()

