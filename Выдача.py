from tkinter import *
from tkinter.ttk import Combobox

from main import return_row, new_cosmetic, return_cabinet, plus_cabinet


def upgrade():
    lbl2 = Label(window, text="Наименование")
    names = return_row("Производство", "Наименование")
    brands = return_row("Производство", "Бренд")
    names_brand = []
    for i in range(len(names)):
        if brands[i] == combo2.get():
            names_brand.append(names[i])

    combo['values'] = names_brand
    lbl7 = Label(window, text="Кабинет", width=50 )

    cabinet_values = return_cabinet()
    cabinet['values'] = cabinet_values

    lbl3 = Label(window, text="Значение", width=50)

    ok = Button(window, text="Добавить", command=add_record)

    lbl2.grid()
    combo.grid()
    lbl7.grid()
    cabinet.grid()
    lbl3.grid()
    ves.grid()

    ok.grid()


def add_record():
    global cabinet, combo, name
    plus_cabinet(cabinet.get(), combo.get(), ves.get())


window = Tk()
window.title("Выдача в производство")
window.geometry('1000x500')


cabinet = Combobox(window)
combo = Combobox(window, width=150)
ves = Entry(window, width=10)

lbl = Label(window, text="Выдача в производство", width=150)
lbl1 = Label(window, text="Бренд", width=50)
combo2 = Combobox(window, width=150)
combo_values2 = return_row("Таблицы", "Бренды")
combo_values2_ok = []
for i in range(len(combo_values2)):
    if combo_values2[i] != 0:
        combo_values2_ok.append(combo_values2[i])
    else:
        break
combo2['values'] = combo_values2_ok

r = Button(text="R", command = upgrade)


lbl.grid()
lbl1.grid()
combo2.grid()
r.grid()


window.mainloop()
