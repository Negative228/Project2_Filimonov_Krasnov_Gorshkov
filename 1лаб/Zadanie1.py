from tkinter import * # подключаем tkinter
# Подключаем модуль с диалоговыми окнами tkinter:
from tkinter.messagebox import *
root = Tk( ) # создаем главное окно
# Устанавливаем минимальные и максимальные размеры окна:
root.minsize(width = 350, height = 150)
root.maxsize(width = 500, height = 300)
root.title("Калькулятор") # заголовок окна

# Создадим 3 фрейма: fr_xy, fr_op и fr_res
# для размещения компонент.
# фрейм fr_xy – компоненты для ввода чисел x, y:
fr_xy = Frame(root)
fr_xy.pack(side = TOP, expand = YES, fill = X)
fr_xy.configure(bg = "blue")
# На нем размещаем две метки и два редактора для ввода чисел x, y:
lx = Label(fr_xy, text = "x = ")
lx.pack(side = LEFT, padx = 10, pady = 10)
lx.configure(fg = "magenta")
entX = Entry(fr_xy)
entX.insert(0, 0) # – в редактор записываем в позицию 0 число 0
entX.pack(side = LEFT, padx = 10, pady = 10)
entX.configure(fg = "magenta")
# Редактор будет выбран при старте (иметь фокус ввода):
entX.focus( )

ly = Label(fr_xy, text = "y = ")
ly.pack(side = LEFT, padx = 10, pady = 10)
ly.configure(fg = "magenta")
entY = Entry(fr_xy)
entY.insert(0, 0)
entY.pack(side = LEFT, padx = 10, pady = 10)
entY.configure(fg = "magenta")
# Создание фрейма с заголовком fr_op – выбор операции:
fr_op = LabelFrame(root, text = "Операция:")
fr_op.pack(side = TOP, expand = YES, fill = X)
fr_op.configure(bg = "blue")
# Операцию будем выбирать с помощью виджета Radiobutton:
oper = ['+', '-', '*', '/'] # – список операций

# Вводим строковую переменную tkinter, ее свяжем с выбором
# Radiobutton
varOper = StringVar( )
# В цикле создаем 4 кнопки Radiobutton (связываем их
# с созданной переменной varOper):
for op in oper:
    Radiobutton(fr_op, text = op, variable = varOper,
                value = op,fg = "magenta").pack(side = LEFT,
                                 padx = 20, pady = 10)
# Устанавливаем текущее значение ‘+’:
varOper.set(oper[0])

# Создаем 3-й фрейм fr_res – вычисление значения
# и вывод результата:
fr_res = Frame(root)
fr_res.pack(side = TOP, expand = YES, fill = BOTH)
fr_res.configure(bg = "blue",cursor = "star")
# Обработчик кнопки:
def OnButtunResult( ):
# Защищенный блок, будем пытаться перевести текст
# из редактора Entry в число:
    try:
        x = float(entX.get()) # извлекаем число из 1-го редактора
    except ValueError:
# если не получилось, выдаем сообщение и выходим:
        showerror("Ошибка заполнения","Переменная x не является числом")
        
        return
# Защищенный блок 2:
    try:
        y = float(entY.get())
    except ValueError:
        showerror("Ошибка заполнения","Переменная y не является числом")
        return
# В переменную op записываем выбранную операцию:
    op = varOper.get( )
# Вычисляем:
    if op == '+': res = x + y
    elif op == '-': res = x - y
    elif op == '*': res = x * y
    elif op == '/':
        
        if y != 0: res = x / y
        else: res = 'NAN'
    else:
        res = 'операция выбрана неправильно'
# Вывод результата на метку:
    lres['text'] = res
# Обработчик кнопки закончился.
# Создаем кнопку и метку, к кнопке присоединяем обработчик:
Button(fr_res, text = "=", width = 10,
       command = OnButtunResult,fg = "magenta").pack(side = LEFT,
                                      padx = 30, pady = 20)
lres = Label(fr_res, text = "")
lres.pack(side = LEFT, padx = 30, pady = 20)
lres.configure(fg = "magenta")
# Запуск цикла обработки сообщений:
root.mainloop( )
