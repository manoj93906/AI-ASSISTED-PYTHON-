def display_weather(city_name):
    import requests
    import json

    api_key = '901bf1ffd34e4c4f6b8c3c95caa747f'  # Replace with your actual API key from OpenWeatherMap
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        weather_data = response.json()
        # Check for API response error (like invalid key, city not found, etc.)
        if weather_data.get('cod') != 200:
            print("Error: Could not connect to API. Check your API key or network connection.")
        else:
            print(json.dumps(weather_data, indent=4))
    except requests.exceptions.Timeout:
        print("Error: Could not connect to API. Check your API key or network connection.")
    except requests.exceptions.RequestException:
        print("Error: Could not connect to API. Check your API key or network connection.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    display_weather(city)
