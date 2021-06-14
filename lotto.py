import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Let The Game Begin!")
root.geometry("1365x768")

img = Image.open("lotto-bg.jpeg")
render = ImageTk.PhotoImage(img)

img = tk.Label(root, image=render)
img.image = render
img.place(x=0,y=0)

pick = tk.Label(root, text = "1st Set: ")
pick.grid(column=1,row=1)

get_pick = tk.Entry(root, width=14)
get_pick.grid(column=2,row=1)

pick_2 = tk.Label(root, text = "2nd Set:")
pick.grid(column=1,row=2)

get_pick2 = tk.Entry(root, width = 14)
get_pick2.grid(column=2,row=2)

b1 = tk.Button(root, text = 1)
b1.grid(column=0,row=2)

b2 = tk.Button(root, text = 2)
b2.grid(column=1,row=2)

b3 = tk.Button(root, text = 3)
b3.grid(column=2,row=2)

b4 = tk.Button(root, text = 4)
b4.grid(column=3,row=2)

b5 = tk.Button(root, text = 5)
b5.grid(column=4,row=2)

b6 = tk.Button(root, text = 6)
b6.grid(column=5,row=2)

root.mainloop()

