from tkinter import *
root = Tk()
root.geometry("800x800")

# img = PhotoImage(file='timer.png').subsample(2, 2)
cnv = Canvas(root, height=500, width=500, bg="white")
cnv.pack()
# second = 0
#
# def seconds():
#     global second
#     cnv.delete("all")
#     cnv.create_image(250, 238,
#                      image=img)
#     cnv.create_text(int(cnv["height"]) / 2, 500 / 2, text=second, )
#     second = second + 1
#     root.after(1000, seconds)
#
# cnv.create_text(int(cnv["height"])/2, 500/2, text=second, )
# cnv.create_image(250, 238,
#                  image=img)
# root.after(1000, seconds)

l = None
p = None


def lkm(event):
    global l
    l = (event.x, event.y)

def pkm(event):
    print("check")
    global p
    p = (event.x, event.y)

def stroi():
    print(l, p)
    cnv.create_line(l[0], l[1], p[0], p[1])

btn = Button(root, text="построить прямую", command=stroi)
btn.pack()

btn.bind("<Button-3>",  pkm)
btn.bind("<Button-1>",  lkm)














root.mainloop()