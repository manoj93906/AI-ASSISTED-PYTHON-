def display_weather(city_name):
    import requests
    import json
    import os

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
        output = {
            "city": city,
            "temp": temp,
            "humidity": humidity,
            "weather": desc.capitalize() if desc else None
        }
        print(json.dumps(output, indent=4))

        # Save/Append weather details to results.json
        filename = "results.json"
        results = []
        if os.path.exists(filename):
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    results = json.load(f)
                    if not isinstance(results, list):
                        results = []
            except (json.JSONDecodeError, IOError):
                results = []
        results.append(output)
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4)

    except requests.exceptions.Timeout:
        print("Error: Could not connect to API. Check your API key or network connection.")
    except requests.exceptions.RequestException:
        print("Error: Could not connect to API. Check your API key or network connection.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    display_weather(city)
