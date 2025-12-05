import requests
import json

def display_weather(city_name):
    api_key = '901bf1ffd34e4c4f6b8c3c95caa747f9'  # Replace with your actual API key from OpenWeatherMap
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Or 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    print(json.dumps(weather_data, indent=4))

if __name__ == "__main__":
    city = input("Enter city name: ")
    display_weather(city)
