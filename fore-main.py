from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Claim Form.")
root.geometry("600x424")
root.config(bg="yellow")

img = Image.open("lotto.jpg")
render = ImageTk.PhotoImage(img)

img = Label(root, image=render)
img.image = render
img.place(x=0,y=0)


bank_acc = Label(root, text = "Bank Account Number")
bank_acc.grid(column=1,row=2)

get_bank = Entry(root, width=15)
get_bank.grid(column=2,row=2)
root.mainloop()
