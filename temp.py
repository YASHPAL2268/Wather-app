# from tkinter import *
# from tkinter import ttk
# import requests
# from datetime import datetime
# from PIL import Image, ImageTk
# import io

# def data_get():
#     city = city_name.get()
#     try:
#         response = requests.get(
#             f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=5fcc819c91c9ac3c0ce10a8b3b3b4bf3"
#         )
#         data = response.json()

#         if response.status_code == 200:
#             w_label1.config(text=data["weather"][0]["main"])
#             wb_label1.config(text=data["weather"][0]["description"])
#             temp_label1.config(text=str(round(data["main"]["temp"] - 273.15, 2)) + " °C")
#             per_label1.config(text=str(data["main"]["pressure"]) + " hPa")
#             humidity_label1.config(text=str(data["main"]["humidity"]) + " %")
#             wind_label1.config(text=str(data["wind"]["speed"]) + " m/s")

#             # Feels Like
#             feels_like = round(data["main"]["feels_like"] - 273.15, 2)
#             feels_like_label1.config(text=f"{feels_like} °C")

#             # Update Time
#             timestamp = data["dt"]
#             time_str = datetime.fromtimestamp(timestamp).strftime('%d-%m-%Y %I:%M %p')
#             time_label1.config(text=time_str)

#             # Weather Icon
#             icon_id = data["weather"][0]["icon"]
#             icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
#             icon_response = requests.get(icon_url)
#             img_data = icon_response.content
#             img = Image.open(io.BytesIO(img_data)).resize((100, 100))
#             icon_photo = ImageTk.PhotoImage(img)
#             icon_label.config(image=icon_photo)
#             icon_label.image = icon_photo  # Keep reference

#         else:
#             for lbl in [w_label1, wb_label1, temp_label1, per_label1, humidity_label1, wind_label1, time_label1, feels_like_label1]:
#                 lbl.config(text="Invalid")
#             icon_label.config(image="", text="No Icon")

#     except:
#         for lbl in [w_label1, wb_label1, temp_label1, per_label1, humidity_label1, wind_label1, time_label1, feels_like_label1]:
#             lbl.config(text="Error")
#         icon_label.config(image="", text="Error")

# # GUI
# win = Tk()
# win.title("Weather App")
# win.config(background="skyblue")
# win.geometry("620x750")

# name_label = Label(win, text="Weather App", font=("Times New Roman", 22, "bold"))
# name_label.place(x=25, y=20, height=50, width=550)

# city_name = StringVar()
# list_name = [
#     "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
#     "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
#     "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan",
#     "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
#     "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu",
#     "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"
# ]
# com = ttk.Combobox(win, values=list_name, font=("Times New Roman", 15), textvariable=city_name)
# com.set("Select City")
# com.place(x=26, y=90, height=50, width=450)

# done_button = Button(win, text="Done", font=("Times New Roman", 20, "bold"), command=data_get)
# done_button.place(x=480, y=90, height=50, width=90)

# # --- Labels ---
# def create_label(y, text):
#     Label(win, text=text, font=("Times New Roman", 18)).place(x=25, y=y, height=40, width=220)
#     lbl = Label(win, text="", font=("Times New Roman", 18))
#     lbl.place(x=260, y=y, height=40, width=300)
#     return lbl

# w_label1 = create_label(160, "Weather")
# wb_label1 = create_label(210, "Description")
# temp_label1 = create_label(260, "Temperature")
# per_label1 = create_label(310, "Pressure")
# humidity_label1 = create_label(360, "Humidity")
# wind_label1 = create_label(410, "Wind Speed")
# time_label1 = create_label(460, "Updated at")
# feels_like_label1 = create_label(510, "Feels Like")

# # Weather Icon
# icon_label = Label(win, bg="skyblue")
# icon_label.place(x=260, y=580, height=100, width=100)

# win.mainloop()



from tkinter import *
from tkinter import ttk, messagebox
import requests
from datetime import datetime
from PIL import Image, ImageTk
import io
import speech_recognition as sr

API_KEY = "5fcc819c91c9ac3c0ce10a8b3b3b4bf3"
favorites = []

# Convert Kelvin to Celsius
def kelvin_to_celsius(temp):
    return round(temp - 273.15, 2)

# Get background color based on weather
def get_weather_color(condition):
    colors = {
        "Clear": "lightyellow", "Clouds": "lightgray",
        "Rain": "lightblue", "Drizzle": "lightblue",
        "Thunderstorm": "gray", "Snow": "white",
        "Mist": "lightgray"
    }
    return colors.get(condition, "skyblue")

# Update background color
def update_background(condition):
    color = get_weather_color(condition)
    win.config(bg=color)
    for widget in win.winfo_children():
        try:
            widget.config(bg=color)
        except:
            pass

# Add to favorites list
def update_favorites(city):
    if city and city not in favorites:
        favorites.append(city)
        favorites_combo["values"] = favorites

# Fetch current weather
def data_get(city=None):
    city = city or city_name.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter or speak a city name.")
        return

    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}")
        data = response.json()

        if response.status_code == 200:
            condition = data["weather"][0]["main"]
            update_background(condition)

            w_label1.config(text=condition)
            wb_label1.config(text=data["weather"][0]["description"])
            temp_label1.config(text=f"{kelvin_to_celsius(data['main']['temp'])} °C")
            per_label1.config(text=f"{data['main']['pressure']} hPa")
            humidity_label1.config(text=f"{data['main']['humidity']} %")
            wind_label1.config(text=f"{data['wind']['speed']} m/s")
            feels_like_label1.config(text=f"{kelvin_to_celsius(data['main']['feels_like'])} °C")

            timestamp = data["dt"]
            time_str = datetime.fromtimestamp(timestamp).strftime('%d-%m-%Y %I:%M %p')
            time_label1.config(text=time_str)

            # Weather icon
            icon_id = data["weather"][0]["icon"]
            icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
            icon_response = requests.get(icon_url)
            img = Image.open(io.BytesIO(icon_response.content)).resize((100, 100))
            icon_photo = ImageTk.PhotoImage(img)
            icon_label.config(image=icon_photo)
            icon_label.image = icon_photo

            update_favorites(city)
        else:
            reset_labels("Invalid")

    except Exception as e:
        print(e)
        reset_labels("Error")

def reset_labels(msg):
    for lbl in [w_label1, wb_label1, temp_label1, per_label1, humidity_label1,
                wind_label1, time_label1, feels_like_label1]:
        lbl.config(text=msg)
    icon_label.config(image="", text=msg)

# Voice search
def voice_search():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("Voice Input", "Speak now...")
        try:
            audio = r.listen(source, timeout=5)
            city = r.recognize_google(audio)
            city_name.set(city)
            data_get(city)
        except:
            messagebox.showerror("Error", "Could not recognize your voice")

# 5-day forecast window
def show_forecast():
    city = city_name.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    try:
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            messagebox.showerror("Error", "Could not fetch forecast data")
            return

        forecast_win = Toplevel(win)
        forecast_win.title(f"{city} - 5 Day Forecast")
        forecast_win.geometry("600x400")
        forecast_win.config(bg="lightblue")

        row = 0
        for item in data["list"]:
            if "12:00:00" in item["dt_txt"]:
                date = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S").strftime("%d %b %Y")
                temp = kelvin_to_celsius(item["main"]["temp"])
                desc = item["weather"][0]["description"]
                Label(forecast_win, text=f"{date} - {temp}°C - {desc}",
                      font=("Arial", 12), bg="lightblue").grid(row=row, column=0, padx=10, pady=5, sticky="w")
                row += 1
    except Exception as e:
        print(e)
        messagebox.showerror("Error", "Failed to load forecast")

# GUI
win = Tk()
win.title("Smart Weather App")
win.geometry("650x800")
win.config(bg="skyblue")

# City input
city_name = StringVar()
Label(win, text="Smart Weather App", font=("Times New Roman", 22, "bold"), bg="skyblue").place(x=25, y=20, height=50, width=600)

ttk.Combobox(win, values=[], font=("Times New Roman", 15), textvariable=city_name).place(x=26, y=90, height=50, width=450)
Button(win, text="Done", font=("Times New Roman", 15, "bold"), command=data_get).place(x=490, y=90, height=50, width=70)
Button(win, text="🎤", font=("Times New Roman", 20), command=voice_search).place(x=570, y=90, height=50, width=50)

# Favorites
Label(win, text="Favorites", font=("Times New Roman", 14), bg="skyblue").place(x=25, y=150, height=30, width=100)
favorites_combo = ttk.Combobox(win, values=favorites, font=("Times New Roman", 12))
favorites_combo.place(x=130, y=150, height=30, width=200)
Button(win, text="Select", command=lambda: data_get(favorites_combo.get())).place(x=340, y=150, height=30, width=80)
Button(win, text="5-Day Forecast", font=("Times New Roman", 12), command=show_forecast).place(x=450, y=150, height=30, width=150)

# Labels
def create_label(y, text):
    Label(win, text=text, font=("Times New Roman", 18), bg="skyblue").place(x=25, y=y, height=40, width=220)
    lbl = Label(win, text="", font=("Times New Roman", 18), bg="skyblue")
    lbl.place(x=260, y=y, height=40, width=300)
    return lbl

w_label1 = create_label(210, "Weather")
wb_label1 = create_label(260, "Description")
temp_label1 = create_label(310, "Temperature")
per_label1 = create_label(360, "Pressure")
humidity_label1 = create_label(410, "Humidity")
wind_label1 = create_label(460, "Wind Speed")
time_label1 = create_label(510, "Updated at")
feels_like_label1 = create_label(560, "Feels Like")
icon_label = Label(win, bg="skyblue")
icon_label.place(x=260, y=620, height=100, width=100)

win.mainloop()
