from tkinter import *
from playsound import playsound

root = Tk()
root.title("Let The Game Begin!")
root.geometry("1365x768")
root.config(bg="yellow")

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
interface.pack(side = RIGHT)

button1 = Button(interface,width=8,text="1",command=listen)
button1.place()

button2 = Button(interface,width=8,text="2")
button2.place()

button3 = Button(interface,width=8,text="3")
button3.place()

button4 = Button(interface,width=8,text="4")
button4.place()

button5 = Button(interface,width=8,text="5")
button5.place()

button6 = Button(interface,width=8,text="6")
button6.place()

button7 = Button(interface,width=8,text="7")
button7.place()

button8 = Button(interface,width=8,text="8")
button8.place()

button9 = Button(interface,width=8,text="9")
button9.place()

button10 = Button(interface,width=8,text="10")
button10.place()

button11 = Button(interface,width=8,text="11")
button11.place()

button12 = Button(interface,width=8,text="12")
button12.place()

button13 = Button(interface,width=8,text="13")
button13.place()

button14 = Button(interface,width=8,text="14")
button14.place()

button15 = Button(interface,width=8,text="15")
button15.place()

button16 = Button(interface,width=8,text="16")
button16.place()

button17 = Button(interface,width=8,text="17")
button17.place()

button18 = Button(interface,width=8,text="18")
button18.place()

button19 = Button(interface,width=8,text="19")
button19.place()

button20 = Button(interface,width=8,text="20")
button20.place()

button21 = Button(interface,width=8,text="21")
button21.place()

button22 = Button(interface,width=8,text="22")
button22.place()

button23 = Button(interface,width=8,text="23")
button23.place()

button24 = Button(interface,width=8,text="24")
button24.place()

button25 = Button(interface,width=8,text="25")
button25.place()

button26 = Button(interface,width=8,text="26")
button26.place()

button27 = Button(interface,width=8,text="27")
button27.place()

button28 = Button(interface,width=8,text="28")
button28.place()

button29 = Button(interface,width=8,text="29")
button29.place()

button30 = Button(interface,width=8,text="30")
button30.place()

button31 = Button(interface,width=8,text="31")
button31.place()

button32 = Button(interface,width=8,text="32")
button32.place()

button33 = Button(interface,width=8,text="33")
button33.place()

button34 = Button(interface,width=8,text="34")
button34.place()

button35 = Button(interface,width=8,text="35")
button35.place()

button36 = Button(interface,width=8,text="36")
button36.place()

button37 = Button(interface,width=8,text="37")
button37.place()

button38 = Button(interface,width=8,text="38")
button38.place()

button39 = Button(interface,width=8,text="39")
button39.place()

button40 = Button(interface,width=8,text="40")
button40.place()

button41 = Button(interface,width=8,text="41")
button41.place()

button42 = Button(interface,width=8,text="42")
button42.place()

button43 = Button(interface,width=8,text="43")
button43.place()

button44 = Button(interface,width=8,text="44")
button44.place()

button45 = Button(interface,width=8,text="45")
button45.place()

button46 = Button(interface,width=8,text="46")
button46.place()

button47 = Button(interface,width=8,text="47")
button47.place()

button48 = Button(interface,width=8,text="48")
button48.place()

button49 = Button(interface,width=8,text="49")
button49.place()

def lotto_result():
        great = Toplevel()
        great.geometry("1005x803")
        great.config(bg="yellow")
        B1 = Button(great, text="Claim Prize")
        B1.pack()
        B2 = Button(great,text="Play Again",command=play_again)
        B2.pack()
        B3 = Button(great,text = "Exit",command=exit)
        B3.pack()

def play_again():
        root.destroy()
        import mains

def exit():
        root.destroy()
        import main

sets_make = Button(root, text = "Play!",width=10,command=lotto_result)
sets_make.place(x=5,y=90)


root.mainloop()

