# Lottery Machine - Lihle Buka
import tkinter as tk
from tkinter import messagebox
import
# initilializing tkinter
root = tk.Tk()
root.title("Gateway Lotto!")
root.geometry("640x320")
root.config(bg="yellow")

number_input = tk.StringVar()
max_len = 13
def length():
    s = number_input.set()
    if len(s) > max_len:
        number_input.set(s[:max_len])

def verify():
    if get_id.get() < "03":
        messagebox.showinfo("Notice","You are too young. Please try again in int(get_name.get() - 18) years.")
    elif get_id.get() >= "03":
        messagebox.showerror("Notice","Let's Play")
        root.destroy()
        import lotto
    elif get_id.get() == "":
             messagebox.showerror("Notice","Invalid ID Number. Try Again")
    else:
        root.destroy()

# detailing the structure
detail = tk.Label(root, text = "Player Details").grid(column = 2,row = 1)

name = tk.Label(root, text = "Name").grid(column = 1,row = 3)
get_name = tk.Entry(root).grid(column=3,row=3)

mail = tk.Label(root, text = "E-mail Address").grid(column=1,row=4)
get_mail = tk.Entry(root).grid(column=3,row=4)

address = tk.Label(root, text = "Address").grid(column=1,row=5)
get_address = tk.Entry(root).grid(column=3,row=5)

id_no = tk.Label(root, text = "ID Number").grid(column=1,row=6)
get_id = tk.Entry(root, textvariable = number_input).grid(column=3,row=6)

play = tk.Button(root,text = "Play!", command=verify).grid(column=2,row=7)

# starting the program
root.mainloop()
