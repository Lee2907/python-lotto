# Lottery Machine - Lihle Buka

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import datetime
import rsaidnumber
from PIL import Image, ImageTk

# initializing tkinter
root = tk.Tk()
root.title("Gateway Lotto!")
root.geometry("775x426")
root.config(bg="yellow")

img = Image.open("Lotto1v3.jpg")
render = ImageTk.PhotoImage(img)

img = tk.Label(root, image=render)
img.image = render
img.place(x=0,y=0)

id_number = rsaidnumber.parse('0207296224083')

detail = tk.Label(root, text = "Player Details").grid(column = 2,row = 1)

name = tk.Label(root, text = "Name").grid(column = 1,row = 3)
get_name = tk.Entry(root).grid(column=3,row=3)

mail = tk.Label(root, text = "Surname").grid(column=1,row=4)
get_mail = tk.Entry(root).grid(column=3,row=4)

address = tk.Label(root, text = "E-mail Address").grid(column=1,row=5)
get_address = tk.Entry(root).grid(column=3,row=5)

id_no = tk.Label(root, text = "ID Number").grid(column=1,row=6)
get_id = tk.Entry(root, textvariable = 13).grid(column=3, row=6)

def verify():
    differ = datetime.today()
    now_date = datetime.timedelta(365.25)
    found = False
try:
    for x in range(len(get_id.get())):
        if int(get_id.get()) >= int(id_number):
            found=True
            if found == True:
                messagebox.showinfo("Notice","Let's Play.")
                import mains
            elif int(get_id.get()) < int(id_number):\
                    messagebox.showwarning("Notice","You are too young to play.")
    else:
        root.destroy()

play = tk.Button(root,text = "Play!").grid(column=2,row=7)

root.mainloop()
