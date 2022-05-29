from tkinter import * 
from tkinter.messagebox import *

root = Tk( ) 
root.minsize(width = 350, height = 125)
root.maxsize(width = 1920, height = 1080)
root.title("Анкетатор 4000 v4.0") 

fr_xy = Frame(root)
fr_xy.pack(side = TOP, expand = YES, fill = X)
fr_xy.configure(bg = "blue")

lx = Label(fr_xy, text = "ФИО:")
lx.pack(side = LEFT, padx = 10, pady = 10)
lx.configure(fg = "magenta")

entName = Entry(fr_xy)
entName.pack(side = LEFT, padx = 10, pady = 10)
entName.configure(fg = "magenta")
entName.focus( )

fr_crs = Frame(root)
fr_crs.pack(side = TOP, expand = YES, fill = X)
fr_crs.configure(bg = "blue")

lcrs = Label(fr_crs, text = "Курс:")
lcrs.pack(side = LEFT, padx = 10, pady = 10)
lcrs.configure(fg = "magenta")

crs = DoubleVar()
course = Scale(fr_crs,width = 10,variable = crs,from_= 1,to = 4,
               orient = "horizontal")
course.pack(anchor = W)

fr_grp = Frame(root)
fr_grp.pack(side = TOP, expand = YES, fill = X)
fr_grp.configure(bg = "blue")

lgrp = Label(fr_grp, text = "Группа:")
lgrp.pack(side = LEFT, padx = 10, pady = 10)
lgrp.configure(fg = "magenta")

grp = DoubleVar()
group = Scale(fr_grp,width = 10,variable = grp,from_= 1,to = 10,
               orient = "horizontal")
group.pack(anchor = W)

fr_res = Frame(root)
fr_res.pack(side = TOP, expand = YES, fill = BOTH)
fr_res.configure(bg = "blue")

def OnButtunResult( ):
    res = "Ваши данные: \n"
    var1 = entName.get()
    var2 = int(crs.get())
    var3 = int(grp.get())
    res += var1 +"\n" + "Курс " + str(var2) + " Группа " + str(var3)
    lres['text'] = res
Button(fr_res, text = "Заполнить данные", width = 14,
       command = OnButtunResult,fg = "magenta").pack(side = LEFT,
                                                     padx = 30, pady = 20)
lres = Label(fr_res, text = "")
lres.pack(side = LEFT,padx = 1, pady = 5)
lres.configure(fg = "magenta")

root.mainloop( )

