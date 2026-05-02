import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'   # Celsius
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if response.status_code == 200:
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            wind = data['wind']['speed']
            desc = data['weather'][0]['description']
            print(f"\n Weather in {city.title()}:")
            print(f"   {desc.capitalize()}")
            print(f"   Temperature: {temp}°C")
            print(f"   Humidity: {humidity}%")
            print(f"   Wind speed: {wind} m/s")
        else:
            print(f"City not found. Error: {data.get('message', 'Unknown error')}")
    except Exception as e:
        print(f"Network error: {e}")

def main():
    if not API_KEY:
        print("Missing OpenWeatherMap API key. Set OPENWEATHER_API_KEY as an environment variable.")
        return

    print("WEATHER DASHBOARD (CLI)")
    while True:
        city = input("\nEnter city name (or 'exit'): ").strip()
        if city.lower() == 'exit':
            break
        if city:
            get_weather(city)

if __name__ == "__main__":
    main()