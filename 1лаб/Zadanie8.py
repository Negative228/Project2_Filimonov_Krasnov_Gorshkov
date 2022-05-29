from tkinter import * 
from tkinter.messagebox import *

root = Tk( ) 
root.minsize(width = 350, height = 125)
root.maxsize(width = 10000, height = 1080)
root.title("Делителятор 2000 v2.0") 

fr_xy = Frame(root)
fr_xy.pack(side = TOP, expand = YES, fill = X)
fr_xy.configure(bg = "blue")

lx = Label(fr_xy, text = "x = ")
lx.pack(side = LEFT, padx = 10, pady = 10)
lx.configure(fg = "magenta")

entX = Entry(fr_xy)
entX.insert(0, 0)
entX.pack(side = LEFT, padx = 10, pady = 10)
entX.configure(fg = "magenta")
entX.focus( )

fr_res = Frame(root)
fr_res.pack(side = TOP, expand = YES, fill = BOTH)
fr_res.configure(bg = "blue")

def OnButtunResult( ):
    try:
        x = int(entX.get())
    except ValueError:
        showerror("Ошибка заполнения","Переменная x не является числом")
        return
    res = ""
    for i in range(1,x//2 + 1):
        if not (x%i):
            res+=str(i)+ "  "
    res+=str(x)
    lres['text'] = res
Button(fr_res, text = "Делители числа", width = 14,
       command = OnButtunResult,fg = "magenta").pack(side = LEFT,
                                                     padx = 30, pady = 20)
lres = Label(fr_res, text = "")
lres.pack(side = LEFT,padx = 1, pady = 5)
lres.configure(fg = "magenta")

root.mainloop( )

