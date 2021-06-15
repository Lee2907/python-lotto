from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("Let The Game Begin!")
root.geometry("1365x768")

style = ttk.Style(root)

style.theme_names()
current_theme = style.theme_use()

style.theme_use("default")

img = Image.open("lotto-bg.jpeg")
render = ImageTk.PhotoImage(img)

img = Label(root, image=render)
img.image = render
img.place(x=0,y=0)
NORM_FONT = ("Verdana",14)
pick = Label(root, text = "Lotto: ")
pick.grid(column=1,row=1)

get_pick = Entry(root, width=14)
get_pick.grid(column=2,row=1)

pick_2 = Label(root, text = "Lotto Plus:")
pick_2.grid(column=1,row=2)

get_pick2 = Entry(root, width = 14)
get_pick2.grid(column=2,row=2)

pick3 = Label(root,text="Powerball: ")
pick3.grid(column=1,row=3)

get_pick3 = Entry(root,width=14)
get_pick3.grid(column=2,row=3)

sets_make = Button(root, text = "Play!",width=10)
sets_make.grid(column=1,row =4)



def popupmsg(msg):
        label = Label(root, text=msg, font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(root, text="Okay", command = lambda:root.destroygen_num)
        B1.pack()

root.mainloop()

