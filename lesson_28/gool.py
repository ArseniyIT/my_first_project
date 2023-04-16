# первая задача

# from tkinter import *
#
# root = Tk()
#
# tekst = Label(root, text="галубай")
# tekst.pack()
#
# ent = Entry(root,
#             width=14)
# ent.pack()
#
# btn1 = Button(root,
#              width=14,
#              bg="red")
# btn1.pack()
#
# btn2 = Button(root,
#              width=14,
#              bg="lightblue")
# btn2.pack()
#
# btn3 = Button(root,
#              width=14,
#              bg="blue")
# btn3.pack()
#
# btn4 = Button(root,
#              width=14,
#              bg="orange")
# btn4.pack()
#
# btn5 = Button(root,
#              width=14,
#              bg="green")
# btn5.pack()
#
# btn6 = Button(root,
#              width=14,
#              bg="yellow")
# btn6.pack()
#
# btn7 = Button(root,
#              width=14,
#              bg="purple")
# btn7.pack()
#
# root.mainloop()



# секонд задача

from tkinter import *

def italic(one):
    lab["font"] = lab["font"].replace('italic', "")
    lab["font"] += " italic"
def bold(two):
    lab["font"] = lab["font"].replace('bold', "")
    lab["font"] += " bold"
def base(three):
    lab["font"] = lab["font"].replace('bold', "").replace('italic', "")

root = Tk()

lab = Label(root, text="Привет")

lab["font"] = "Arial 15"

lab.pack()

lkm = lab.bind("<Button-1>", bold)
pkm = lab.bind("<Button-3>", italic)
dlkm = lab.bind("<Double-Button-1>", base)


root.mainloop()










