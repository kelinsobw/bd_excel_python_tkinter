import tkinter
from tkinter import *

from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import ttk

from main import return_row, new_cosmetic, return_cabinet, plus_cabinet, return_xyz, return_cabitet_cosmetic



def choise_cosmetic2(cabinet, names_brand):
    root = tk.Tk()
    root.geometry('1600x800')
    container = ttk.Frame(root)
    #Label(root, text="Взвешивание").grid()
    canvas = tk.Canvas(container, width=1500, height=600)
    # create canvas in the container frame
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    # create scrollbar in container frame
    scrollable_frame = ttk.Frame(canvas)
    # define the scrollable frame in canvas

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    # this is due that methods: pack(), place() and grid() can't be used for scrollbars
    # so a windows containing scrollable_frame is created in canvas

    canvas.configure(yscrollcommand=scrollbar.set)
    names = return_row("Производство", "Наименование")
    brands = return_row("Производство", "Бренд")
    names_brand = []
    for i in range(len(names)):
        if brands[i] == combo2.get():
            names_brand.append(names[i])
    x=0
    names_plus = []
    ves_plus = []
    for item in names_brand:
        frame_my = LabelFrame(scrollable_frame)
        frame_my.grid()
        for i in range(2):
            if i==0:
                e = Label(frame_my, text=item, width=100, anchor="w")
                e.grid(row=x, column=i)
                names_plus.append(item)
            if i==1:
                e = Entry(frame_my, width=100, )
                e.grid(row=x, column=i)
                ves_plus.append(e)

        x = x + 1
    print(names_plus)
    print(ves_plus)
    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    save_bt = Button(root, text="Сохранить", command=lambda: add_record(names_plus, ves_plus, cabinet))
    save_bt.pack(side=BOTTOM)
    root.mainloop()


def add_record(names_plus, ves_plus, cabinet):
    ves = []
    for item in ves_plus:
        ves.append(item.get())
    for i in range(len(names_plus)):
        if str(ves[i])!="":
            plus_cabinet(cabinet, names_plus[i], int(ves[i]))


window = Tk()
window.title("Выдача в производство")
window.geometry('500x500')


cabinet = Combobox(window)
ves = Entry(window, width=10)

lbl = Label(window, text="Выдача в производство", width=50)
lbl1 = Label(window, text="Бренд", width=50)
combo2 = Combobox(window, width=50)
combo_values2 = return_row("Таблицы", "Бренды")
combo_values2_ok = []
for i in range(len(combo_values2)):
    if combo_values2[i] != 0:
        combo_values2_ok.append(combo_values2[i])
    else:
        break
combo2['values'] = combo_values2_ok


lbl.grid()
lbl1.grid()
combo2.grid()
names = return_row("Производство", "Наименование")
brands = return_row("Производство", "Бренд")
names_brand = []
for i in range(len(names)):
    if brands[i] == combo2.get():
        names_brand.append(names[i])

lbl7 = Label(window, text="Кабинет", width=50)

cabinet_values = return_cabinet()
cabinet['values'] = cabinet_values

lbl3 = Label(window, text="Значение", width=50)

ok = Button(window, text="Добавить", command=lambda: choise_cosmetic2(cabinet.get(), ves.get()))

lbl7.grid()
cabinet.grid()



ok.grid()

window.mainloop()
