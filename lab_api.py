import requests
import subprocess


TOKEN = '17022056ef216f6855bf3864f51b2a7c'
OS = 'WINDOWS'

if OS == 'WINDOWS':
    from win10toast import ToastNotifier
 

class WeatherAPI:

    token = ''
    base_url = 'http://api.openweathermap.org'
    coord_url = '/geo/1.0/direct'
    weather_url = '/data/2.5/weather'

    def __init__(self, city='Moscow', country='Russia', lg='ru'):
        self.city = city
        self.country = country
        self.language = lg

    def request_details(self):
        params = {
            'q': f'{self.city},{ self.country}',
            'limit': 1,
            'appid': self.token
            }
        url = f'{self.base_url}{self.coord_url}'
        details = requests.get(url, params=params)
        data = details.json()[0]
        self.retrieve_coordinates(data)

    def retrieve_coordinates(self, data):
        self.lat = data['lat']
        self.lon = data['lon']

    def request_weather(self):
        params = {
             'lat': self.lat,
             'lon': self.lon,
             'units': 'metric',
             'appid': self.token,
             'lang': self.language
         }
        url = f'{self.base_url}{self.weather_url}'
        weather = requests.get(url, params=params)
        self.weather = weather.json()
    
    def string_weather(self):
        city = self.weather['name']
        temp = self.weather['main']['temp']
        weather = self.weather['weather'][0]
        details = weather['description'].capitalize()
        return f'{city} {temp}°C\n{details}'

    def show(self):
        title, details = self.string_weather().split('\n')
        if OS == 'LINUX':
            subprocess.Popen(['notify-send',
                               title,
                               details
                            ])
        elif OS == 'WINDOWS':
            toaster = ToastNotifier()
            toaster.show_toast(title, details)

    def show_console(self):
        print(self.string_weather())


if __name__ == '__main__':
    WeatherAPI.token = TOKEN
    weather = WeatherAPI()
    weather.request_details()
    weather.request_weather()
    weather.show_console()
    weather.show()

