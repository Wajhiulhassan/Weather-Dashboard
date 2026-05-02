import datetime
import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
UNIT_OPTIONS = {
    'c': 'metric',
    'f': 'imperial',
    'k': ''
}
UNIT_SYMBOLS = {
    'metric': '°C',
    'imperial': '°F',
    '': 'K'
}
WIND_UNITS = {
    'metric': 'm/s',
    'imperial': 'mph',
    '': 'm/s'
}


def format_time(timestamp, tz_offset):
    utc_time = datetime.datetime.utcfromtimestamp(timestamp)
    local_time = utc_time + datetime.timedelta(seconds=tz_offset)
    return local_time.strftime('%H:%M')


def get_weather(city, units):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': units
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()
        if response.status_code == 200:
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            wind_speed = data['wind']['speed']
            visibility = data.get('visibility', 0)
            desc = data['weather'][0]['description']
            timezone_offset = data.get('timezone', 0)
            sunrise = format_time(data['sys']['sunrise'], timezone_offset)
            sunset = format_time(data['sys']['sunset'], timezone_offset)
            unit_symbol = UNIT_SYMBOLS[units]
            wind_unit = WIND_UNITS[units]

            print(f"\nWeather in {city.title()} ({units or 'Kelvin'}):")
            print(f"  {desc.capitalize()}")
            print(f"  Temperature: {temp}{unit_symbol}")
            print(f"  Feels like: {feels_like}{unit_symbol}")
            print(f"  Humidity: {humidity}%")
            print(f"  Pressure: {pressure} hPa")
            print(f"  Wind speed: {wind_speed} {wind_unit}")
            print(f"  Visibility: {visibility} m")
            print(f"  Sunrise: {sunrise}")
            print(f"  Sunset: {sunset}")
        else:
            print(f"City not found. Error: {data.get('message', 'Unknown error')}")
    except requests.exceptions.Timeout:
        print("Request timed out. Please check your internet connection and try again.")
    except Exception as e:
        print(f"Network error: {e}")


def show_help():
    print("\nCommands:")
    print("  help          - Show this help menu")
    print("  units         - Change temperature units (C/F/K)")
    print("  exit          - Quit the app")
    print("  <city name>   - Get weather for a city")


def choose_units():
    while True:
        choice = input("Choose units (C=°C, F=°F, K=Kelvin): ").strip().lower()
        if choice in UNIT_OPTIONS:
            return UNIT_OPTIONS[choice]
        print("Invalid option. Enter C, F, or K.")


def main():
    if not API_KEY:
        print("Missing OpenWeatherMap API key. Set OPENWEATHER_API_KEY as an environment variable.")
        return

    current_units = 'metric'
    print("WEATHER DASHBOARD (Version 3)\n")
    show_help()
    print(f"\nCurrent units: {current_units} ({UNIT_SYMBOLS[current_units]})")

    while True:
        user_input = input("\nEnter city name or command: ").strip()
        if not user_input:
            continue
        command = user_input.lower()
        if command == 'exit':
            break
        if command == 'help':
            show_help()
            continue
        if command == 'units':
            current_units = choose_units()
            print(f"Units set to: {current_units} ({UNIT_SYMBOLS[current_units]})")
            continue
        get_weather(user_input, current_units)


if __name__ == "__main__":
    main()
