
# # from tkinter import *
# # from tkinter import ttk

# # import requests

# # def data_get():
# #  city=city_name.get()   
# #  data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+" &appid=5fcc819c91c9ac3c0ce10a8b3b3b4bf3").json()
# #  w_label1.config(text=data["weather"][0]["main"])
# #  wb_label1.config(text=data["weather"][0]["description"])
# #  temp_label1.config(text=str(data["main"]["temp"]-273.15))
# #  per_label1.config(text=data["main"]["pressure"])








# # win = Tk()

# # win.title("Chaudhary Yashpal")
# # win.config(background="blue")
# # win.geometry("600x600")

# # name_label = Label(win, text="Chaudhary Yashpal  Weather App",
# #                    font=("Times New Roman", 20, "bold"))


# # name_label.place(x=25, y=50, height=50, width=450)  

# # city_name=StringVar
# # list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]


# # com = ttk.Combobox(win, text="Chaudhary Yashpal  Weather App",values=list_name,
# #                    font=("Times New Roman", 20, "bold")),textvariable=city_name
# # com.place(x=25, y=120, height=50, width=450)  










# # w_label = Label(win, text="Weather Climate",
# #                 font=("Times New Roman", 20))
# # w_label.place(x=25, y=260, height=50, width=220)

# # w_label1 = Label(win, text="",
# #                 font=("Times New Roman", 20))
# # w_label1.place(x=250, y=260, height=50, width=220)





# # wb_label = Label(win, text="Weather Description",
# #                 font=("Times New Roman", 17))
# # wb_label.place(x=25, y=330, height=50, width=220)

# # wb_label1 = Label(win, text="",
# #                 font=("Times New Roman", 17))
# # wb_label1.place(x=250, y=330, height=50, width=220)







# # temp_label = Label(win, text="Tempreture",
# #                 font=("Times New Roman", 20))
# # temp_label.place(x=25, y=400, height=50, width=220)

# # temp_label1 = Label(win, text="",
# #                 font=("Times New Roman", 20))
# # temp_label1.place(x=250, y=400, height=50, width=220)





# # per_label = Label(win, text="Pressure",
# #                 font=("Times New Roman", 20))
# # per_label.place(x=25, y=470, height=50, width=220)

# # per_label1 = Label(win, text="",
# #                 font=("Times New Roman", 20))
# # per_label1.place(x=250, y=470, height=50, width=220)


# # done_button=Button(win, text="Done",
# #                    font=("Times New Roman", 20, "bold"))
# # done_button.place(y=190,height=50,width=100,x=200)



# # win.mainloop()


# from tkinter import *
# from tkinter import ttk
# import requests

# def data_get():
#     city = city_name.get()
#     data = requests.get(
#         "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=5fcc819c91c9ac3c0ce10a8b3b3b4bf3"
#     ).json()

#     w_label1.config(text=data["weather"][0]["main"])
#     wb_label1.config(text=data["weather"][0]["description"])
#     temp_label1.config(text=str(round(data["main"]["temp"] - 273.15, 2)) + " °C")
#     per_label1.config(text=str(data["main"]["pressure"]) + " hPa")

# win = Tk()
# win.title(" Weather App :")
# win.config(background="blue")
# win.geometry("610x610")

# name_label = Label(win, text=" Weather App",
#                    font=("Times New Roman", 20, "bold"))
# name_label.place(x=25, y=50, height=50, width=550)

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
# com.place(x=26, y=120, height=50, width=450)

# done_button = Button(win, text="Done", font=("Times New Roman", 20, "bold"), command=data_get)
# done_button.place(x=480, y=120, height=50, width=90)

# w_label = Label(win, text="Weather Climate", font=("Times New Roman", 20))
# w_label.place(x=25, y=200, height=50, width=220)

# w_label1 = Label(win, text="", font=("Times New Roman", 20))
# w_label1.place(x=250, y=200, height=50, width=300)

# wb_label = Label(win, text="Weather Description", font=("Times New Roman", 17))
# wb_label.place(x=25, y=270, height=50, width=220)

# wb_label1 = Label(win, text="", font=("Times New Roman", 17))
# wb_label1.place(x=250, y=270, height=50, width=300)

# temp_label = Label(win, text="Temperature", font=("Times New Roman", 20))
# temp_label.place(x=25, y=340, height=50, width=220)

# temp_label1 = Label(win, text="", font=("Times New Roman", 20))
# temp_label1.place(x=250, y=340, height=50, width=300)

# per_label = Label(win, text="Pressure", font=("Times New Roman", 20))
# per_label.place(x=25, y=410, height=50, width=220)

# per_label1 = Label(win, text="", font=("Times New Roman", 20))
# per_label1.place(x=250, y=410, height=50, width=310)

# win.mainloop()

from tkinter import *
from tkinter import ttk
import requests
from datetime import datetime

def data_get():
    city = city_name.get()
    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=5fcc819c91c9ac3c0ce10a8b3b3b4bf3"
        )
        data = response.json()

        if response.status_code == 200:
            w_label1.config(text=data["weather"][0]["main"])
            wb_label1.config(text=data["weather"][0]["description"])
            temp_label1.config(text=str(round(data["main"]["temp"] - 273.15, 2)) + " °C")
            per_label1.config(text=str(data["main"]["pressure"]) + " hPa")
            humidity_label1.config(text=str(data["main"]["humidity"]) + " %")
            wind_label1.config(text=str(data["wind"]["speed"]) + " m/s")

            # Optional: Show update time
            timestamp = data["dt"]
            time_str = datetime.fromtimestamp(timestamp).strftime('%d-%m-%Y %I:%M %p')
            time_label1.config(text=time_str)

        else:
            for lbl in [w_label1, wb_label1, temp_label1, per_label1, humidity_label1, wind_label1, time_label1]:
                lbl.config(text="Invalid")
    except:
        for lbl in [w_label1, wb_label1, temp_label1, per_label1, humidity_label1, wind_label1, time_label1]:
            lbl.config(text="Error")

win = Tk()
win.title("Weather App")
win.config(background="skyblue")
win.geometry("620x700")

name_label = Label(win, text="Weather App", font=("Times New Roman", 22, "bold"))
name_label.place(x=25, y=20, height=50, width=550)

city_name = StringVar()
list_name = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
    "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
    "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan",
    "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
    "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu",
    "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"
]
com = ttk.Combobox(win, values=list_name, font=("Times New Roman", 15), textvariable=city_name)
com.set("Select City")
com.place(x=26, y=90, height=50, width=450)

done_button = Button(win, text="Done", font=("Times New Roman", 20, "bold"), command=data_get)
done_button.place(x=480, y=90, height=50, width=90)

# --- Labels ---
def create_label(y, text):
    Label(win, text=text, font=("Times New Roman", 18)).place(x=25, y=y, height=40, width=220)
    lbl = Label(win, text="", font=("Times New Roman", 18))
    lbl.place(x=260, y=y, height=40, width=300)
    return lbl

w_label1 = create_label(160, "Weather")
wb_label1 = create_label(210, "Description")
temp_label1 = create_label(260, "Temperature")
per_label1 = create_label(310, "Pressure")
humidity_label1 = create_label(360, "Humidity")
wind_label1 = create_label(410, "Wind Speed")
time_label1 = create_label(460, "Updated at")

win.mainloop()
