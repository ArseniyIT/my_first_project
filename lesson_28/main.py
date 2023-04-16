from tkinter import *

def h_ell_o(event):
    message = ent.get() #прием значения из Entry
    ent.delete(0, END)  # очистить значение
    print(message)


root = Tk() #создание/иницидлизация
root.geometry("500x400")
root.title("My first window")
root["bg"] = "lightpink"

lab = Label(root, text="Standoff2") # надпись
lab.pack() # размещаем элемент (по порядку)

# lab["background"] = "pink"
# lab["foreground"] = "red"
lab["bg"] = "pink" # ключевым словом
lab["fg"] = "#29defe" # hex цвет
# lab["font"] = 30 # 1: размер шрифта
# lab["font"] = "Arial 20 bold" # мульти значение
lab["font"] = ("Arial", 20, "bold", "italic", "underline", "overstrike") # мульти значение кортежами
lab["height"] = 1
lab["width"]= 8

btn = Button(root,text="My first button",
             bg = "lightblue",
             font = 30,
             # command = h_ell_o
             )
btn.pack()
btn.bind("<Button-1>", h_ell_o)
# Button-1 = ЛКМ
# Button-3 = ПКМ
# Double-Button-3 = ПКМ * 2

ent = Entry(root,
            width=16,
            font=25,
            bd=20)
ent.pack()

txt = Text(root,
           width=20,
           height=5,
           wrap="word")
# wrap
# word - перенос по словам
# char - посимволам
# none - без переноса

txt.pack()







root.mainloop() # отрисовка окна
# здесб не присать. размотрено. отказано. без права на обжалование.