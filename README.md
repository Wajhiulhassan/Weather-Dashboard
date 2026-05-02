# Weather Dashboard CLI (Version 3)

A Python command-line weather dashboard that fetches current weather data from the OpenWeatherMap API. Version 3 adds unit selection, a help menu, and more detailed weather output.

## What is new in Version 3

- Added temperature units selection: Celsius, Fahrenheit, or Kelvin
- Added a help menu with commands
- Expanded weather output to include:
  - Feels like temperature
  - Pressure
  - Visibility
  - Sunrise and sunset times
- Better error handling for network timeouts and invalid city names

## Files

- `weather.py` — main Python script for the weather dashboard
- `requirements.txt` — required external Python package
- `README.md` — project documentation

## Requirements

- Python 3.x
- `requests` library
- Internet connection
- OpenWeatherMap API key

## How to run

1. Install the required Python library:

```powershell
python -m pip install -r requirements.txt
```

2. Set your OpenWeatherMap API key:

```powershell
setx OPENWEATHER_API_KEY "your_api_key_here"
```

3. Restart PowerShell or open a new terminal.
4. Change to the `Weather-Dashboard` folder:

```powershell
cd "E:\CYBERSECURITY\All Semester\Programming Project\Weather-Dashboard"
```

5. Run:

```powershell
python weather.py
```

## Commands

- `help` — Show the command menu
- `units` — Change temperature units to Celsius, Fahrenheit, or Kelvin
- `exit` — Close the dashboard
- `<city name>` — Get weather for the entered city

## Example session

```text
WEATHER DASHBOARD (Version 3)

Commands:
  help          - Show this help menu
  units         - Change temperature units (C/F/K)
  exit          - Quit the app
  <city name>   - Get weather for a city

Current units: metric (°C)

Enter city name or command: London

Weather in London (metric):
  Broken clouds
  Temperature: 12°C
  Feels like: 10°C
  Humidity: 67%
  Pressure: 1016 hPa
  Wind speed: 4.1 m/s
  Visibility: 10000 m
  Sunrise: 05:18
  Sunset: 20:31
```

## Notes

- `OPENWEATHER_API_KEY` must be set in your environment before running the script.
- The app supports three unit modes:
  - `C` for Celsius
  - `F` for Fahrenheit
  - `K` for Kelvin
- This version includes expanded weather details and safer API key handling.

## Important

- Do not hardcode your API key into `weather.py` if you plan to upload this project to GitHub.
- Keep your `.gitignore` or use environment variables to protect sensitive values.
