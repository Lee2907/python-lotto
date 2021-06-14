from tkinter import *
from tkinker import messagebox

root = Tk()
root.title("Claim Form.")
root.geometry("640x320")
root.config(bg="yellow")

acc_name = Label(root, text = "Account Holder")
acc_name.grid(column=1,row=1)

get_acc = Entry(root)
get_acc.grid(column=2,row=1)

bank_acc = Label(root, text = "Bank Account Number")
bank_acc.grid(column=1,row=2)

root.mainloop()
