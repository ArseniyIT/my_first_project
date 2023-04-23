from tkinter import *

# def action():
#     print("salam")



root = Tk()
root.geometry("400x300")
root["bg"]="green"

# lab = Label(root, text="данил манкей", bg="red", fg="#228337", font="bold 15")
#
# lab.pack()
#
# ent = Entry(root, width=15, bor=10, font="Arial 15 bold")
# ent.pack()
#
# txt = Text(root, width=18, height=5, font="Arial 15 bold", wrap="word")
# txt.pack()
#
# btn = Button(root, text="отправить", bg="yellow", command=action)
# btn.pack()

# def get_cb():
#     print(cb_val.get())
#
# cb_val = BooleanVar()
#
# cb = Checkbutton(root, text="я дед инсайд", command=get_cb, variable=cb_val, onvalue=True, offvalue=False)
# cb.pack()
# cb.select() # .select()-поставить галочку
# cb.deselect() # .deselect()-убрать галочку

# def get_rb():
#     print(rb_val.get())
#
# rb_val = IntVar()
# rb1 = Radiobutton(root, text="sogl", variable=rb_val, value=421, command=get_rb)
# rb1.pack()
#
# rb2 = Radiobutton(root, text="sogl", variable=rb_val, value=23, command=get_rb)
# rb2.pack()
#
#
#
# def get_scala(val):
#     print(sc.get())
#     print(val)
#
# sc = Scale(root, from_=0, to=15, orient="horizontal", length=150, tickinterval=2, resolution=3, command=get_scala)
# sc.pack()
# ph = PhotoImage(file="goole1000-7.png")
# ph_big = ph.zoom(3,3)
# ph_small = ph.subsample(2,2) # .subsample() - уменьшение
# ph_poltora = ph.subsample(3, 3).zoom(2, 2)
# lb3 = Label(root, image=ph_poltora)
# lb3.pack()
Label(root, text="baran", bg="pink").pack()
Label(root, text="osel", bg="lightblue").pack(pady=15)


root.mainloop()