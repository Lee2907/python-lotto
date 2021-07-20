# Lottery Machine - Lihle Buka

import tkinter as tk
from tkinter import messagebox
import playsound
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

font_stylize = ("Verdana",11)

# structuring the form
detail = tk.Label(root, text = "Player Details",font=font_stylize).grid(column = 2,row = 1)

name = tk.Label(root, text = "Name",font=font_stylize).grid(column = 1,row = 3)
get_name = tk.Entry(root).grid(column=3,row=3)

surname = tk.Label(root, text = "Surname",font=font_stylize).grid(column=1,row=4)
get_surname = tk.Entry(root).grid(column=3,row=4)

address = tk.Label(root, text = "E-mail Address",font=font_stylize).grid(column=1,row=5)
get_address = tk.Entry(root).grid(column=3,row=5)

id_no = tk.Label(root, text = "ID Number",font=font_stylize).grid(column=1,row=6)
get_id = tk.Entry(root, textvariable = 13).grid(column=3, row=6)

my_text = open("list.txt","a+")
my_text.write("Name of player: " + get_name.get() |"Surname: " + get_surname.get() | "E-mail Address: " + get_address.get() | "ID Number: " + str(get_id.get()) + "\n")
my_text.close()

# the implementation of functions
def mail_valid():
        email = get_address.get()

        if "@" in email:
            messagebox.showinfo("Congrats", "Thanks for taking the first step. And have a good time.")
        else:
            messagebox.showinfo("Notice","Our system noticed an error in the e-mail address you provided. Please enter a more accurate one.")

def id_verify():
        try:
            Id = int(get_id.get())
            id_ls = get_id.get()

            year = get_id.get()[1]
            year2 = get_id.get()[0:2]

            lotto_file = open('Lotto_file.txt', 'a+')
            lotto_file.write("Name: " + get_name.get() + "| Player Email: " + get_address.get() + "| Player ID: " + str(get_id.get()) + "\n",)
            lotto_file.write("\n")
            lotto_file.close()

            if type(Id) == type(str()) or len(id_ls) != 13:
                raise ValueError
            elif int(year) <= 3:

                messagebox.showinfo(title="Let's Play!", message="Lets Play!")
                playsound('win_song.wav')
                root.destroy()
            elif int(year2) > 3 and int(year2) > 21:
                messagebox.showinfo(title="Let's Play!", message="Lets Play!")
                playsound('win_song.wav')
                root.destroy()
                import lottoplay
            else:
                x = int(year) - 3
                messagebox.showinfo(title="Under Age", message="Your are too young to play")
        except ValueError:

            messagebox.showerror(title="Invalid Id", message="Please enter valid ID")
            get_id.delete(0)

#the button
play = tk.Button(root,text = "Play!",font=font_stylize,command=id_verify).grid(column=2,row=7)

#starting the form
root.mainloop()
