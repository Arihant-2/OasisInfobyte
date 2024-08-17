from tkinter import *
import requests
from datetime import datetime

# Initialize Window
app = Tk()
app.geometry("450x450")  # Size of the window
app.resizable(0, 0)  # Fix the window size
app.title("Weather App")

# ---------------------- Functions to fetch and display weather info
city_input = StringVar()

def format_time(utc_time):
    local_time = datetime.utcfromtimestamp(utc_time)
    return local_time.strftime('%H:%M:%S')

def fetch_weather():
    api_key = "e7b5099e5f6abd30c205894ceebdf8f1"  # Sample API key
    city = city_input.get()
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    
    response = requests.get(weather_url)
    weather_data = response.json()

    output_field.delete("1.0", "end")  # Clear the text field for each new output

    if weather_data['cod'] == 200:  # 200 is meant that html request has responed properly
        kelvin_offset = 273
        temperature = int(weather_data['main']['temp'] - kelvin_offset)  # Convert Kelvin to Celsius
        feels_like = int(weather_data['main']['feels_like'] - kelvin_offset)
        pressure = weather_data['main']['pressure']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed'] * 3.6  # Convert m/s to km/h
        cloudiness = weather_data['clouds']['all']
        weather_description = weather_data['weather'][0]['description']

        weather_report = (
            f"\nCity: {city}\n"
            f"Temperature: {temperature}°C\n"
            f"Feels Like: {feels_like}°C\n"
            f"Pressure: {pressure} hPa\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed:.2f} km/h\n"
            f"Cloudiness: {cloudiness}%\n"
            f"Description: {weather_description.capitalize()}\n"
        )
    else:
        report = f"\nWeather for '{city}' not found!\nPlease enter a valid city name."

    output_field.insert(INSERT, report)  # Display the weather report

# ------------------------------ Frontend part of code - Interface

city_label = Label(app, text='Enter City Name:', font='Times_New_Roman 12 bold')
city_label.pack(pady=10)

city_entry = Entry(app, textvariable=city_input, width=28, font='Arial 14 bold')
city_entry.pack()

check_weather_button = Button(
    app, command=fetch_weather, text="Check Weather", font="Times_New_Roman 10", 
    bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5
)
check_weather_button.pack(pady=20)

weather_label = Label(app, text="Weather Details:", font='Arial 12 bold')
weather_label.pack(pady=10)

output_field = Text(app, width=50, height=10)
output_field.pack()

app.mainloop()
