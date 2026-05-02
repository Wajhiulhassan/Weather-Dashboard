import datetime
import os
import requests
import tkinter as tk
from tkinter import ttk, messagebox

API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
UNIT_OPTIONS = {
    'Celsius (°C)': 'metric',
    'Fahrenheit (°F)': 'imperial',
    'Kelvin (K)': ''
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


class WeatherDashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Dashboard v4")
        self.root.geometry("520x500")
        self.root.resizable(False, False)

        self.style = ttk.Style(root)
        self.style.theme_use('clam')
        self.style.configure('TButton', font=('Segoe UI', 10), padding=6)
        self.style.configure('TLabel', font=('Segoe UI', 10))
        self.style.configure('Header.TLabel', font=('Segoe UI', 14, 'bold'))
        self.style.configure('Status.TLabel', font=('Segoe UI', 9), foreground='gray25')

        self.create_widgets()

    def create_widgets(self):
        header = ttk.Label(self.root, text="Weather Dashboard v4", style='Header.TLabel')
        header.pack(pady=(16, 8))

        input_frame = ttk.Frame(self.root)
        input_frame.pack(padx=16, pady=8, fill='x')

        city_label = ttk.Label(input_frame, text="City:")
        city_label.grid(row=0, column=0, sticky='w')

        self.city_entry = ttk.Entry(input_frame, width=32)
        self.city_entry.grid(row=0, column=1, padx=8, sticky='w')
        self.city_entry.focus()

        unit_label = ttk.Label(input_frame, text="Units:")
        unit_label.grid(row=1, column=0, pady=(10, 0), sticky='w')

        self.unit_var = tk.StringVar(value='Celsius (°C)')
        self.unit_menu = ttk.Combobox(input_frame, textvariable=self.unit_var, state='readonly', values=list(UNIT_OPTIONS.keys()), width=19)
        self.unit_menu.grid(row=1, column=1, pady=(10, 0), sticky='w')

        button_frame = ttk.Frame(self.root)
        button_frame.pack(padx=16, pady=8, fill='x')

        self.search_btn = ttk.Button(button_frame, text="Get Weather", command=self.on_search)
        self.search_btn.pack(side='left', padx=(0, 8))

        self.clear_btn = ttk.Button(button_frame, text="Clear", command=self.clear_output)
        self.clear_btn.pack(side='left')

        self.status_label = ttk.Label(self.root, text="Enter a city and click Get Weather.", style='Status.TLabel')
        self.status_label.pack(pady=(4, 12), anchor='w', padx=18)

        self.output_frame = ttk.Frame(self.root)
        self.output_frame.pack(padx=16, pady=6, fill='both', expand=True)

        self.output_text = tk.Text(self.output_frame, height=18, wrap='word', font=('Segoe UI', 10), state='disabled', bg='#f7f7f7')
        self.output_text.pack(fill='both', expand=True)

        footer = ttk.Label(self.root, text="Powered by OpenWeatherMap API", style='Status.TLabel')
        footer.pack(side='bottom', pady=(4, 10))

    def set_status(self, message, error=False):
        self.status_label.config(text=message, foreground='red' if error else 'gray25')

    def clear_output(self):
        self.output_text.config(state='normal')
        self.output_text.delete('1.0', tk.END)
        self.output_text.config(state='disabled')
        self.set_status("Enter a city and click Get Weather.")

    def on_search(self):
        city = self.city_entry.get().strip()
        if not city:
            self.set_status("Please enter a city name.", error=True)
            return
        if not API_KEY:
            self.set_status("No OpenWeatherMap API key found. Set OPENWEATHER_API_KEY in your environment.", error=True)
            return

        units_label = self.unit_var.get()
        units = UNIT_OPTIONS.get(units_label, 'metric')
        self.fetch_weather(city, units)

    def fetch_weather(self, city, units):
        self.set_status("Loading weather data...")
        params = {
            'q': city,
            'appid': API_KEY,
            'units': units
        }
        try:
            response = requests.get(BASE_URL, params=params, timeout=10)
            data = response.json()
            if response.status_code == 200:
                self.display_weather(city, data, units)
            else:
                self.set_status(f"Error: {data.get('message', 'City not found')}", error=True)
        except requests.exceptions.Timeout:
            self.set_status("Request timed out. Check your connection.", error=True)
        except Exception as exc:
            self.set_status(f"Network error: {exc}", error=True)

    def display_weather(self, city, data, units):
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        visibility = data.get('visibility', 0)
        desc = data['weather'][0]['description']
        tz_offset = data.get('timezone', 0)
        sunrise = format_time(data['sys']['sunrise'], tz_offset)
        sunset = format_time(data['sys']['sunset'], tz_offset)
        unit_symbol = UNIT_SYMBOLS[units]
        wind_unit = WIND_UNITS[units]

        text = (
            f"Weather in {city.title()} ({self.unit_var.get()}):\n"
            f"{desc.capitalize()}\n\n"
            f"Temperature: {temp}{unit_symbol}\n"
            f"Feels like: {feels_like}{unit_symbol}\n"
            f"Humidity: {humidity}%\n"
            f"Pressure: {pressure} hPa\n"
            f"Wind speed: {wind_speed} {wind_unit}\n"
            f"Visibility: {visibility} m\n"
            f"Sunrise: {sunrise}\n"
            f"Sunset: {sunset}\n"
        )
        self.output_text.config(state='normal')
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, text)
        self.output_text.config(state='disabled')
        self.set_status("Weather data loaded successfully.")


if __name__ == '__main__':
    root = tk.Tk()
    app = WeatherDashboardApp(root)
    root.mainloop()
