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


root.mainloop()

