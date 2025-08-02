from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=752e6d686bb50fd3f965f1b478fff52a").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("App")
win.config(bg="deepskyblue")

 
name_label = Label(win,text="Weather App",
                   font=("Times New Roman",70,"bold"))
name_label.place(x=375,y=30,height=150,width=800)              


city_name = StringVar()
list_name = indian_states = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh",
                            "Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab",
                            "Rajasthan","Sikkim", "Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]
com = ttk.Combobox(win,values=list_name,font=("Times New Roman",25,"bold"),textvariable= city_name)
com.place(x=620,y=200,height=75,width=350)



w_label = Label(win,text="Weather Climate",
                font=("Times New Roman",18,))
w_label.place(x=460,y=395,height=40,width=255)

w_label1 = Label(win,text="",
                font=("Times New Roman",18,))
w_label1.place(x=875,y=395,height=40,width=255)



wb_label = Label(win,text="Weather Description",
                font=("Times New Roman",18,))
wb_label.place(x=460,y=465,height=40,width=255)

wb_label1 = Label(win,text="",
                font=("Times New Roman",18,))
wb_label1.place(x=875,y=465,height=40,width=255)



temp_label = Label(win,text="Temperature",
                font=("Times New Roman",18,))
temp_label.place(x=460,y=535,height=40,width=255)

temp_label1 = Label(win,text="",
                font=("Times New Roman",18,))
temp_label1.place(x=875,y=535,height=40,width=255)



per_label = Label(win,text="Pressure",
                font=("Times New Roman",20,))
per_label.place(x=460,y=605,height=40,width=255)

per_label1 = Label(win,text="",
                font=("Times New Roman",20,))
per_label1.place(x=875,y=605,height=40,width=255)



done_button = Button(win,text="Done",
                   font=("Times New Roman",15,"bold"),command=data_get)
done_button.place(x=750,y=300,height=50,width=100,)



win.mainloop()