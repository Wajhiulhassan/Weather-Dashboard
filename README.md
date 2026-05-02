# Weather Dashboard UI (Version 4)

A Python desktop weather dashboard with a graphical user interface (UI) built using tkinter. Version 4 introduces a modern UI/UX experience with unit selection, live status updates, and a clear results display.

## What is new in Version 4

- Fully graphical UI with buttons, inputs, and result panel
- Unit selection for Celsius, Fahrenheit, and Kelvin
- Status feedback for loading, errors, and success
- Clear display of weather details in a styled panel
- Improved UX for searching and clearing results

## Files

- `weather.py` — main Python application with Tkinter UI
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

5. Run the UI application:

```powershell
python weather.py
```

## UI Features

- Enter a city name and click **Get Weather**
- Choose between **Celsius**, **Fahrenheit**, or **Kelvin**
- Click **Clear** to reset the output panel
- See a status message for loading, errors, or success

## Weather details shown

- Description
- Temperature
- Feels like temperature
- Humidity
- Pressure
- Wind speed
- Visibility
- Sunrise and sunset times

## Notes

- `OPENWEATHER_API_KEY` must be set in your environment before running the app.
- The UI is built with tkinter and works on Windows.
- Do not hardcode your API key into `weather.py` if you upload this project to GitHub.
