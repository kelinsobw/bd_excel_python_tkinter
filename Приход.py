from tkinter import *
from tkinter.ttk import Combobox

from main import return_row, new_cosmetic, add_cosmetic


def add_record():
    record = [combo2.get()]
    record.append(combo.get())
    record.append(cout.get())
    record.append(price.get())
    add_cosmetic(record)


window = Tk()
window.title("Приход")
window.geometry('400x500')

lbl = Label(window, text="Приход")
lbl1 = Label(window, text="Бренд")
combo2 = Combobox(window)
combo_values2 = return_row("Таблицы", "Бренды")
combo2['values'] = combo_values2
lbl2 = Label(window, text="Наименование")
combo = Combobox(window)
combo_values = return_row("Производство", "Наименование")
combo['values'] = combo_values
lbl3 = Label(window, text="Количество")
cout = Entry(window,width=10)
lbl4 = Label(window, text="Стоимость")
price = Entry(window,width=10)
ok = Button(window, text="Добавить", command=add_record)

lbl.grid()
lbl1.grid()
combo2.grid()
lbl2.grid()
combo.grid()
lbl3.grid()
cout.grid()
lbl4.grid()
price.grid()
ok.grid()

window.mainloop()
