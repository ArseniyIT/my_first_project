from tkinter import *
root = Tk()
root.geometry("800x800")

# cnv = Canvas(root, height=500, width=500, bg="green")
# cnv.pack(anchor=CENTER, expand=True)

# ===========TEXT=============
# cnv.create_text(10,10,
#     text="данил редановец",
#     anchor=NW,
#     font="bold 23",
#     fill="pink")

#==========RECTANGLE==============
# cnv.create_rectangle(10,10,
#                      150, 100,
#                      fill="blue",
#                      outline="red",
#                      width=15)

#=========POLYGON=============
# cnv.create_polygon(10, 10,
#                    150, 150,
#                    10, 150)

#=========OVAL===============
# cnv.create_oval(10,10,
#                 150,150)

#==========ARC===========
# cnv.create_arc(10,10,
#                150,150,
#                extent=-140,
#                start=45,
#                style=CHORD) # хорда

# cnv.create_arc(10,10,
#                150,150,
#                extent=-140,
#                start=45,
#                style=ARC,
#                outline="red",
#                width=15,
#                dash=".")

# event
def sam(event):
    print(f"это координата по x: {event.x}, а это координата по y: {event.y}")

btn = Button(root, text="sam takoi")
btn.pack()
btn.bind("<Button-3>", sam)

# отрисовка




root.mainloop()