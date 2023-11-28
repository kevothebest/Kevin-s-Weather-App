import tkinter as tk
import requests
from tkinter import font


def getweather(city):
    weatherkey = 'ef0dac46ead1b7ace70b3903798cd050'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    paras= {"APPID":weatherkey,'q':city, 'units':'metric'}
    response=requests.get(url,params=paras)
    weather=response.json()
    label1['text']=formatresponse(weather)


def formatresponse(weather):
    try:
        name=weather['name']
        description=weather['weather'][0]['description']
        temp=weather['main']['temp']
        wind=weather['wind']['speed']
        finalstr="Name: %s \nDescription: %s \nWind: %s \nTemperature: %s °C" %(name, description, wind, temp)
    except:
        finalstr="Something went wrong"
    return finalstr
root=tk.Tk()

width=600
height=500


canvas=tk.Canvas(height=height,width=width)
canvas.pack()

frame1=tk.Frame(root,bg="#0080ff",bd=5)
frame1.place(relx=0.5,rely=0.1,relwidth=0.7,relheight=0.1,anchor="n")

entry1=tk.Entry(frame1,font=40)
entry1.place(relwidth=0.7,relheight=1)

button1=tk.Button(frame1,text='Get The Weather',command=lambda:getweather(entry1.get()))
button1.place(relx=0.7,relheight=1,relwidth=0.3)

frame2=tk.Frame(root,bg='#0080ff',bd=5)
frame2.place(relx=0.5,rely=0.3,relwidth=0.7,relheight=0.6,anchor='n')

label1=tk.Label(frame2,font=("Times New Roman",20),anchor='nw',justify='left',bd=5)
label1.place(relheight=1,relwidth=1)








root.mainloop()