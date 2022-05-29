from tkinter import * 
from tkinter.messagebox import *
from random import randrange

root = Tk( ) 
root.minsize(width = 350, height = 125)
root.maxsize(width = 1920, height = 1080)
root.title("Сумматор 3000 v3.0") 

fr_main = Frame(root)
fr_main.configure(bg = "blue")
e = [[],[],[]]
for i in range(3):
    for j in range(3):
        e[i].append(Entry(width=10))
        e[i][j].insert(0,randrange(1,100))
        e[i][j].grid(row=i, column=j)

def OnButtunResult( ):
    res = 0
    for i in range(3):
        for j in range(3):
            res+=int(e[i][j].get())
    lres['text'] = res
Button(root, text = "Получить сумму",
       command = OnButtunResult,fg = "magenta").grid(row = 4,column = 1)
lres = Label(root, text = "")
lres.grid(row = 5, column = 1)
lres.configure(fg = "magenta")

root.mainloop( )

