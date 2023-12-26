import requests
import json
from tkinter import Tk, Label
from PIL import Image, ImageTk
from io import BytesIO

# Задание 1
website_url = "https://ya.ru"
response = requests.get(website_url)
print("Response from Yandex:")
print(response.text)

# Задание 2
def get_weather(city_name):
    api_key = "28218bc18c36461dc6dfcbb7e12392b0"  

    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(weather_url)

    if response.status_code == 200:
        weather_data = response.json()
        print("\nWeather Information:")
        print(f"City: {weather_data['name']}")
        print(f"Weather: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']} K")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Pressure: {weather_data['main']['pressure']} hPa")
    else:
        print(f"Failed to get weather information. Status code: {response.status_code}")


# Example
city_name = "Moscow"
get_weather(city_name)


# Задание 3 
api_url = "http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/"
game_id = input('Введите ID игры (Ex. 367520 (Hollow Night)): ')
number_news = int(input('Введите количество новостей: '))
api_params = {"appid": game_id, "count": number_news, "maxlength": 150, "format": "json"}

api_response = requests.get(api_url, params=api_params)
if api_response.status_code == 200:
    api_data = api_response.json()
    
    for news in api_data['appnews']['newsitems']:
        print(f'\n{news["title"]} | {news["url"]}')
        print(f'{news["feedlabel"]} {news["author"]} | Дата: {news["date"]}')
        print(f'{news["contents"]}')
        print('\n')
        
else:
    print(f"Failed to get API information. Status code: {api_response.status_code}")

# Доп Задание

class NASAImageGenerator:
    def __init__(self, root, api_key):
        self.root = root
        self.root.title("NASA Image of the Day")
        self.api_key = api_key
        self.current_date = ""
        self.label = Label(root)
        self.label.pack(padx=10, pady=10)
        self.load_image()

    def load_image(self):
        url = f"https://api.nasa.gov/planetary/apod?api_key={self.api_key}&date={self.current_date}"
        response = requests.get(url)
        data = response.json()

        image_url = data.get("url", "")
        date = data.get("date", "")

        if image_url and date != self.current_date:
            self.current_date = date
            self.display_image(image_url)

    def display_image(self, image_url):
        response = requests.get(image_url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((400, 400), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)

        self.label.configure(image=photo)
        self.label.image = photo

if __name__ == "__main__":
    api_key = "xQyJaR6tutXothSe8NsWLf2r7qBs0gxubYBgiXw4"  # Замените на свой ключ API NASA
    root = Tk()
    app = NASAImageGenerator(root, api_key)
    root.mainloop()