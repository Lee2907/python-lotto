from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import requests

root = Tk()
root.title("Currency Converter")
root.geometry("1200x1240")


font_stylize = ("Verdana",11)

value = StringVar()

information = requests.get('https://v6.exchangerate-api.com/v6/3b6104d9c62069d198e73219/latest/USD')
information_json = information.json()
conversion_rate = information_json['conversion_rates']

my_earnings = Label(root, text="Your Earning")
my_earnings.place(x=10, y=50)
earning_entry = Entry(root, textvariable=value, width=10)
earning_entry.place(x=100, y=50)
my_label3 = Label(root, text="Choose a Currency:")
my_label3.place(x=10, y=90)

convert_list = Listbox(root, width=20)
for i in conversion_rate.keys():
    convert_list.insert(END, str(i))
    convert_list.place(x=25, y=125)

def converting():
        num = float(earning_entry.get())
        ans = num * information_json['conversion_rates'][convert_list.get(ACTIVE)]
        my_label3['text'] = ans

convert_btn = Button(root, command=converting, text="Convert", font=10, bg="royal blue", fg="white")
convert_btn.place(x=10, y=315)

root.mainloop()
