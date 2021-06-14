# Lottery Machine - Lihle Buka
import tkinter as tk
from tkinter import messagebox

# initilializing tkinter
lotto = tk.Tk()
lotto.geometry("640x320")
lotto.config(bg="peachpuff")

number_input = tk.StringVar()

def input():
    get_id.set(lotto)
def verify():
     if get_name
         messagebox.showinfo("Notice","Let's Play.")



# detailing the structure
detail = tk.Label(lotto, text = "Player Details").grid(column = 2,row = 1)

name = tk.Label(lotto, text = "Name").grid(column = 1,row = 3)
get_name = tk.Entry(lotto).grid(column=3,row=3)

mail = tk.Label(lotto, text = "E-mail Address").grid(column=1,row=4)
get_mail = tk.Entry(lotto).grid(column=3,row=4)

address = tk.Label(lotto, text = "Address").grid(column=1,row=5)
get_address = tk.Entry(lotto).grid(column=3,row=5)

id_no = tk.Label(lotto, text = "ID Number").grid(column=1,row=6)
get_id = tk.Entry(lotto).grid(column=3,row=6)

play = tk.Button(lotto,text = "Play!").grid(column=2,row=7)

# starting the program
lotto.mainloop()
