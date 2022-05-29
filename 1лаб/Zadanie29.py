from tkinter import *
from math import * # подключаем математические функции
from tkinter.messagebox import * # подключаем диалоговые окна
root = Tk( )
root.title("Методы eval и exec")
# создаем фрейм для размещения компонент задающих x, y:
win1 = Frame(root)
win1.pack(anchor = "n", expand = YES, fill = X)
lx = Label(win1, text = "x = ")
lx.pack(side = LEFT, padx = 10, pady = 10)
entX = Entry(win1)
entX.insert(0, 0)

entX.pack(side = LEFT, padx = 10, pady = 10)
entX.focus( )
ly = Label(win1, text = "y = ")
ly.pack(side = LEFT, padx = 10, pady = 10)
entY = Entry(win1)
entY.insert(0, 0)
entY.pack(side = LEFT, padx = 10, pady = 10)
# создаем второй фрейм для задания функции и вычисления:
win2 = Frame(root)
win2.pack(anchor = "n", expand = YES, fill = X)
Label(win2, text = "Функция: ").pack(side = LEFT,padx = 10, pady = 10)

entF = Entry(win2)
entF.pack(side = LEFT, padx = 10, pady = 10, expand = YES,
fill = X)
entF.insert(0, "x or y")
# Создаем обработчик кнопки:
def res( ):
    try:
        x = entX.get()
    except ValueError:
        showerror("Ошибка заполнения","Переменная x не является целым числом")
        return
    try:
        y = entY.get()

    except ValueError:
        showerror("Ошибка заполнения","Переменная y не является целым числом")
        return
    X = []
    for i in x:
        if i != ' ':
            X.append(int(i))
    Y = []
    for i in y:
        if i != ' ':
            Y.append(int(i))
    F = entF.get( ) # считываем текст из редактора
    for i in range(len(X), 0, -1):
        tmp = 'x' + str(i)
        F = F.replace(tmp, str(X[i - 1]))
    for i in range(len(Y), 0, -1):
        tmp = 'y' + str(i)
        F = F.replace(tmp, str(Y[i - 1]))
    labF['text'] = eval(F) # выполняем его и результат
# записываем на метку
# Создаем кнопку и метку:
Button(win2, text = 'Вычислить',
       command = res).pack(side = LEFT,
                           padx = 10, pady = 5)
labF = Label(win2, text = " ")
labF.pack(side = LEFT, padx = 10, pady = 10)
root.mainloop()
