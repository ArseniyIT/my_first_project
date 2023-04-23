# from tkinter import *
#
# def gool(event):
#     message = ent.get()
#     lab["text"] = message
#
# root = Tk()
# root.geometry("300x200")
# lb = Label(root, text="...")
# lb.pack()
#
# ent = Entry(root)
# ent.bind("<Button-3>", gool)
# ent.insert("Вставь и ПКМ")
# ent.pack()
# root.mainloop()

from tkinter import *
#
# def hel_lo():
#     user_choose = rb_val.get()
#     if user_choose == 1:
#         lab["text"] = "Hello " + rb1["text"]
#     else:
#         lab["text"] = "Hello " + rb2["text"]
#
#
# root = Tk()
# root.geometry("300x200")
#
#
# lab = Label(root, text="Hello")
# lab.pack()
#
#
# rb_val = IntVar()
#
# rb1 = Radiobutton(root, text="World", variable=rb_val, value=1, command=hel_lo)
# rb1.pack()
#
# rb2 = Radiobutton(root, text="Python", variable=rb_val, value=2, command=hel_lo)
# rb2.pack()
#
#
# root.mainloop()

# from tkinter import *
#
# def activation():
#     if cb_val.get() == True:
#         b["text"] = "Активна"
#         b["state"] = "normal"
#     else:
#         b["text"] = "Не активна"
#         b["state"] = "disabled"
#
# root = Tk()
# cb_val = BooleanVar()
# cb = Checkbutton(root, text="активировать", variable=cb_val, onvalue=True, offvalue=False, command=activation )
# cb.pack()
#
# b = Button(root, text="Не активен", state="disabled")
# b.pack()
#
#
# root.mainloop()