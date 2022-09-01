from tkinter import *
from tkinter.ttk import Combobox

from main import return_row, new_cosmetic


def add_record():
    record = [combo2.get()]
    record.append(combo.get())
    record.append(name.get())
    record.append(volume.get())
    record.append(weight.get())
    record.append(price.get())
    new_cosmetic(record)


window = Tk()
window.title("Добавить продукт")
window.geometry('400x500')

lbl = Label(window, text="Добавить продукт")
lbl1 = Label(window, text="Группа")
combo2 = Combobox(window)
combo_values2 = return_row("Таблицы", "Группы")
combo2['values'] = combo_values2
lbl2 = Label(window, text="Бренд")
combo = Combobox(window)
combo_values = return_row("Таблицы", "Бренды")
combo['values'] = combo_values
lbl3 = Label(window, text="Наименование")
name = Entry(window,width=10)
lbl4 = Label(window, text="Обьем")
volume = Entry(window,width=10)
lbl5 = Label(window, text="Вес")
weight = Entry(window,width=10)
lbl6 = Label(window, text="Цена")
price = Entry(window,width=10)
ok = Button(window, text="Добавить", command=add_record)

lbl.grid()
lbl1.grid()
combo2.grid()
lbl2.grid()
combo.grid()
lbl3.grid()
name.grid()
lbl4.grid()
volume.grid()
lbl5.grid()
weight.grid()
lbl6.grid()
price.grid()
ok.grid()

window.mainloop()
