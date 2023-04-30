from tkinter import *
from random import randint
root = Tk()
root.geometry("700x700")


# lb = Label(root, text="Логин:")
# lb.grid(column=0, row=0)
#
# lb1 = Label(root, text="Пароль:")
# lb1.grid(column=0, row=1)
#
# ent = Entry(root)
# ent.grid(column=1, row=0)
#
# ent = Entry(root, show="*")
# ent.grid(column=1, row=1)
#
#
# btn = Button(root, text="print('print')")
# btn.grid(column=1, row=2, sticky=E)

from tkinter import messagebox

def win():
    messagebox.showinfo(message="ты редановец!")

def privet(event):
    btn.place(x=randint(0, 600), y=randint(0, 600))



btn = Button(root, text="кто клинет тот редановец!", bg="pink", command=win)
btn.place(x=10, y=10)
btn.bind("<Enter>", privet)






root.mainloop()