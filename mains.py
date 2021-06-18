import random
from tkinter import *
from playsound import playsound
from PIL import Image, ImageTk

root = Tk()
root.title("Let The Game Begin!")
root.geometry("1365x768")
root.config(bg="yellow")

NORM_FONT = ("Arial",12)

img = Image.open("daily-lotto.jpeg")
render = ImageTk.PhotoImage(img)

img = Label(root, image=render)
img.image = render
img.place(x=0,y=0)

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

act = Button(root, text = "Open")
act.place(x=135,y=5)

act2 = Button(root, text = "Open")
act2.place(x=145,y=30)

act3 = Button(root, text = "Open")
act3.place(x=211,y=55)

interface = Frame(root)
interface.config(bg="yellow")
interface.pack(side=LEFT)

button1 = Button(interface,text="1")
button1.pack(side=LEFT)

button2 = Button(interface,text="2")
button2.pack(side=LEFT)

button3 = Button(interface,text="3")
button3.pack(side=LEFT)

button4 = Button(interface,text="4")
button4.pack(side=LEFT)

button5 = Button(interface,text="5")
button5.pack(side=LEFT)

button6 = Button(interface,text="6")
button6.pack(side=LEFT)

button7 = Button(interface,text="7")
button7.pack(side=LEFT)

button8 = Button(interface,text="8")
button8.pack(side=LEFT)

button9 = Button(interface,text="9")
button9.pack(side=LEFT)

button10 = Button(interface,text="10")
button10.pack(side=LEFT)

button11 = Button(interface,text="11")
button11.pack(side=LEFT)

button12 = Button(interface,text="12")
button12.pack(side=LEFT)

button13 = Button(interface,text="13")
button13.pack(side=LEFT)

button14 = Button(interface,text="14")
button14.pack(side=LEFT)

button15 = Button(interface,text="15")
button15.pack(side=LEFT)

button16 = Button(interface,text="16")
button16.pack(side=LEFT)

button17 = Button(interface,text="17")
button17.pack(side=LEFT)

button18 = Button(interface,text="18")
button18.pack(side=LEFT)

button19 = Button(interface,text="19")
button19.pack(side=LEFT)

button20 = Button(interface,text="20")
button20.pack(side=LEFT)

button21 = Button(interface,text="21")
button21.pack(side=LEFT)

button22 = Button(interface,text="22")
button22.pack(side=LEFT)

button23 = Button(interface,text="23")
button23.pack(side=LEFT)

button24 = Button(interface,text="24")
button24.pack(side=LEFT)

button25 = Button(interface,text="25")
button25.pack(side=LEFT)

button26 = Button(interface,text="26")
button26.pack(side=LEFT)

button27 = Button(interface,text="27")
button27.pack(side=LEFT)

button28 = Button(interface,text="28")
button28.pack(side=LEFT)

button29 = Button(interface,text="29")
button29.pack(side=LEFT)

button30 = Button(interface,text="30")
button30.pack(side=LEFT)

button31 = Button(interface,text="31")
button31.pack(side=LEFT)

button32 = Button(interface,text="32")
button32.pack(side=LEFT)

button33 = Button(interface,text="33")
button33.pack(side=BOTTOM)

button34 = Button(interface,text="34")
button34.pack()

button35 = Button(interface,text="35")
button35.pack()

button36 = Button(interface,text="36")
button36.pack()

button37 = Button(interface,text="37")
button37.pack()

button38 = Button(interface,text="38")
button38.pack()

button39 = Button(interface,text="39")
button39.pack()

button40 = Button(interface,text="40")
button40.pack()

button41 = Button(interface,text="41")
button41.pack()

button42 = Button(interface,text="42")
button42.pack()

button43 = Button(interface,text="43")
button43.pack()

button44 = Button(interface,text="44")
button44.pack()

button45 = Button(interface,text="45")
button45.pack()

button46 = Button(interface,text="46")
button46.pack()

button47 = Button(interface,text="47")
button47.pack()

button48 = Button(interface,text="48")
button48.pack()

button49 = Button(interface,text="49")
button49.pack()

def random_num():
        random.randint(0,50)

def lotto_result():
        great = Toplevel()
        great.title("Winner's Scoresheet")
        great.geometry("1005x803")
        great.config(bg="yellow")
        info = Label(great, text="Congratulations, you have won.")
        info.pack()
        B1 = Button(great, text="Claim Prize")
        B1.pack()
        B2 = Button(great,text="Play Again",command=play_again)
        B2.pack()
        B3 = Button(great,text = "Exit",command=exit)
        B3.pack()

def play_again():
        root.withdraw()
        import mains

def exit():
        root.destroy()
        import main

sets_make = Button(root, text = "Play!",width=10,command=lotto_result)
sets_make.place(x=5,y=90)


root.mainloop()

