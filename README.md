# Weather Dashboard CLI

A simple Python command-line weather dashboard that fetches current weather data using the OpenWeatherMap API.

## What it does

- Prompts the user for a city name
- Requests current weather data from OpenWeatherMap
- Displays weather description, temperature, humidity, and wind speed
- Supports repeated city lookups until the user types `exit`

## Files

- `weather.py` — main Python script for the weather dashboard
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

2. Optionally set your OpenWeatherMap API key:

```powershell
setx OPENWEATHER_API_KEY "your_api_key_here"
```

3. Open PowerShell or Command Prompt in the `Weather-Dashboard` folder.
4. Run:

```powershell
python weather.py
```

5. Enter a city name when prompted.
6. Type `exit` to quit.

## Example

```text
WEATHER DASHBOARD (CLI)

Enter city name (or 'exit'): London

 Weather in London:
   Clear sky
   Temperature: 15°C
   Humidity: 60%
   Wind speed: 3.5 m/s
```

## Notes

- The script uses metric units (Celsius) for temperature.
- If the city is not found, an error message is shown.
- If there is a network issue, a network error message is displayed.

## Customize

- To use your own OpenWeatherMap API key, replace the `API_KEY` value in `weather.py` with your key.
