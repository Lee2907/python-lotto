# Lottery Machine - Lihle Buka

import tkinter as tk
from tkinter import messagebox
import playsound
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

font_stylize = ("Verdana",11)
listen = playsound("click.mp3")

id_number = rsaidnumber.parse('0207296224083')
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

my_text = open("list.txt","w")
# the implementation of functions
def mail_valid():
        person = get_name.get()
        email = str(get_address.get())

        if ".com" in get_address.get():
            messagebox.showinfo("Congrats", "Thanks for taking the first step. And have a good time.")
        else:
            messagebox.showinfo("Notice","Our system noticed an error in the e-mail address you provided. Please enter a more accurate one.")
            get_address.delete(0)
def verify():
    try:
        for x in range(len(str(get_id))):
            if str(get_id.get()) >= int(id_number.valid):
                found=True
            if found == True:
                messagebox.showinfo("Notice","Let's Play.")
                import lottoplay
            elif str(get_id.get()) < int(id_number.valid):
                    messagebox.showwarning("Notice","You are too young to play.")
            else:
                messagebox.showerror("Notice","Invaliid ID Number. Try again.")
    except AttributeError:
        import lottoplay
#the button
play = tk.Button(root,text = "Play!",font=font_stylize,command=verify).grid(column=2,row=7)

#starting the form
root.mainloop()
