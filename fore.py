from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Claim Form.")
root.geometry("612x459")
root.config(bg="yellow")

img = Image.open("win.jpg")
render = ImageTk.PhotoImage(img)

img = Label(root, image=render)
img.image = render
img.place(x=0,y=0)


bank_acc = Label(root, text = "Bank Account Number")
bank_acc.grid(column=1,row=2)

get_bank = Entry(root, width=15)
get_bank.grid(column=2,row=2)

acc_detail = Label(root, text = "Account Details")
acc_detail.grid(column=1,row=3)

get_det = Entry(root, width = 15)
get_det.grid(column=2,row=3)

banks = ['Capitec', 'ABSA', 'FNB','Standard Bank']
variable = StringVar(root)
variable.set(banks[0])

choose_bank = OptionMenu(root,variable,*banks)
choose_bank.config(height=1,width=6,font=('Arial',14))
choose_bank.grid(column=1,row=5)

claim = Button(root, text = "Claim Away!", width=10)
claim.grid(column=1,row=6)

root.mainloop()
