def display_weather(city_name):
    import requests

    api_key = '901bf1ffd34e4c4f6b8c3c95caa747f9'  # Replace with your actual API key
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)
        if response.status_code == 404:
            print("Error: City not found. Please enter a valid city.")
            return
        response.raise_for_status()
        weather_data = response.json()
        if str(weather_data.get('cod')) != '200':
            print("Error: City not found. Please enter a valid city.")
            return
        city = weather_data.get('name', 'Unknown')
        temp = weather_data.get('main', {}).get('temp')
        humidity = weather_data.get('main', {}).get('humidity')
        desc = ""
        if weather_data.get('weather') and isinstance(weather_data['weather'], list) and len(weather_data['weather']) > 0:
            desc = weather_data['weather'][0].get('description', '')
        print(f"City: {city}")
        if temp is not None:
            print(f"Temperature: {temp}°C")
        else:
            print("Temperature: N/A")
        if humidity is not None:
            print(f"Humidity: {humidity}%")
        else:
            print("Humidity: N/A")
        print(f"Weather: {desc.capitalize() if desc else 'N/A'}")
    except requests.exceptions.Timeout:
        print("Error: Could not connect to API. Check your API key or network connection.")
    except requests.exceptions.RequestException:
        print("Error: Could not connect to API. Check your API key or network connection.")

# Example usage:
if __name__ == "__main__":
    city = input("Enter city name: ")
    display_weather(city)
