import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from playsound import playsound
from PIL import Image, ImageTk

root = Tk()
root.title("Let The Game Begin!")
root.geometry("1305x803")

img = Image.open("daily-lotto.jpeg")
render = ImageTk.PhotoImage(img)

img = Label(root, image=render)
img.image = render
img.place(x=0,y=0)

results = ["R0", "R20", "R100,50", "R2 384", "R8 584", "R10 000 000"]

NORM_FONT = ("Arial",12)
listen = playsound("click.mp3")

pick = Label(root, text = "Lotto: ",font=NORM_FONT)
pick.place(x=5,y=5)
                
get_pick = Entry(root, width=14)
get_pick.place(x=50,y=5)
                
pick_2 = Label(root, text = "Lotto Plus:",font=NORM_FONT)
pick_2.place(x=5,y=30)
                
get_pick2 = Entry(root, width = 14)
get_pick2.place(x=81,y=30)
                
pick3 = Label(root,text="Powerball: ",font=NORM_FONT)
pick3.place(x=5,y=56)
                
get_pick3 = Entry(root,width=14)
get_pick3.place(x=91,y=57)

interface = Frame(root)
interface.pack(side=TOP)

def entry():
        get_pick.insert(0,1)
        get_pick2.insert(0,1)
        get_pick3.insert(0,1)

button0 = Button(root,text="0",command=entry)
button0.pack(side=LEFT)

button1 = Button(root,text="1",command=entry)
button1.pack(side=LEFT)

button2 = Button(root,text="2",command=entry)
button2.pack(side=LEFT)

button3 = Button(root,text="3",command=entry)
button3.pack(side=LEFT)

button4 = Button(root,text="4",command=entry)
button4.pack(side=LEFT)

button5 = Button(root,text="5",command=entry)
button5.pack(side=LEFT)

button6 = Button(root,text="6",command=entry)
button6.pack(side=LEFT)
                
button7 = Button(root,text="7",command=entry)
button7.pack(side=LEFT)
                
button8 = Button(root,text="8",command=entry)
button8.pack(side=LEFT)
                
button9 = Button(root,text="9",command=entry)
button9.pack(side=LEFT)

buttonn = Button(root,text=",",command=entry)
buttonn.pack(side=LEFT)

def lotto_result():
        great = Toplevel()
        great.title("Winner's Scoresheet")
        great.geometry("1005x803")
        great.config(bg="yellow")
        def results_lottery():
                catalogs = [get_pick,get_pick2,get_pick3]
                random.sample(1,49)
                catalogs += 1
                if catalogs <= 1:
                        return "You have won R0. Sorry, better luck next time."
                elif catalogs == 2:
                        return "You have won R20. You could win big next time!"
                elif catalogs == 3:
                        return "You have won R100.50. You could win big next time!"
                elif catalogs == 4:
                       return "You have won R2 384. Congratulations, maybe next time you could win even more."
                elif catalogs == 5:
                        return "You have won R8 584. Congratulations, maybe next time you could win even more."
                elif catalogs == 6:
                        return "You have won R10 000 000. Congratulations!!!!"
        B1 = Button(great, text="Claim Prize",command=go_ahead)
        B1.pack()
        B2 = Button(great,text="Play Again",command=play_again)
        B2.pack()
        B3 = Button(great,text = "Exit",command=exit)
        B3.pack()

def go_ahead():
        confirm = messagebox.askokcancel("Confirmation","This is just to make sure that you agree with the terms & conditions of the prize provision.")
        if confirm == "ok":
                root.destroy()
                import fore
def play_again():
        root.withdraw()
        import lottoplay

def exit():
        root.destroy()
        import start

sets_make = Button(root, text = "Play!",width=10,command=lotto_result)
sets_make.place(x=5,y=90)

root.mainloop()

