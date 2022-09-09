import tkinter
from tkinter import *

from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import ttk

from main import return_row, new_cosmetic, add_cosmetic, return_cabinet, return_cabitet_cosmetic, save_in_file, \
    return_xyz


def save(entries, name, meaning):
    meaning_now = []
    for item in entries:
        meaning_now.append(item.get())
    save_in_file(name, meaning, meaning_now, str(combo2.get()), str(combo.get()))


def delete_cosmetic(entries):
    for item in entries:
        item.destroy()


def choise_cosmetic2(entries):
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


    global entry
    cosmitin_cab = return_cabitet_cosmetic(combo2.get())
    name = []
    meaning = []


    x = 0

    for item in cosmitin_cab:
        if str(cosmitin_cab.get(item)) != "0" or cosmitin_cab.get(item) != 0:
            frame_my = LabelFrame(scrollable_frame)
            frame_my.grid()
            for i in range(3):
                if i==0:
                    e = Label(frame_my, text=item, width=100, anchor="w")
                    e.grid(row=x, column=i)
                    name.append(item)
                if i == 1:
                    e = Entry(frame_my, )
                    e.insert(0, cosmitin_cab.get(item))
                    e.grid(row=x, column=i)
                    meaning.append(cosmitin_cab.get(item))
                    entries.append(e)
                if i==2:
                    e = Label(frame_my, text=return_xyz(item), width=10, anchor="w")
                    e.grid(row=x, column=i)

        x = x + 1

    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    save_bt = Button(root, text="Сохранить", command=lambda: save(entries, name, meaning))
    save_bt.pack(side=BOTTOM)
    root.mainloop()


def choise_cosmetic(entries):
    global entry
    cosmitin_cab = return_cabitet_cosmetic(combo2.get())
    name = []
    meaning = []
    i = 7

    canvas = tkinter.Canvas(window, borderwidth=0, )
    frame = tkinter.Frame(canvas, )
    vsb = tkinter.Scrollbar(window, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)
    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4, 4), window=frame, anchor="nw")

    for item in cosmitin_cab:
        if str(cosmitin_cab.get(item)) != "0" or cosmitin_cab.get(item) != 0:
            label=Label(frame, text=item, )
            label.pack(fill='both')
            #entries.append((label))
            name.append(item)
            entry = Entry(frame, width=10)
            entry.insert(0, cosmitin_cab.get(item))
            meaning.append(cosmitin_cab.get(item))
            entry.pack(expand=True, )
            entries.append(entry)
            i = i+1

    save_bt = Button(frame, text="Сохранить", command=lambda: save(entries, name, meaning))
    save_bt.pack()
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))


window = Tk()
window.title("Взвешивание")
window.geometry('400x300')

cosmitin_cab = {}
lbl = Label(window, text="Взвешивание")
lbl0 = Label(window, text="Выберите мастера")
combo = Combobox(window)
combo_values = return_row("Мастера", "Фамилия Имя")
combo['values'] = combo_values
lbl1 = Label(window, text="Выберите кабинет")
combo2 = Combobox(window)
combo_values2 = return_cabinet()
combo2['values'] = combo_values2
entries = []
ok = Button(window, text="Вывести косметику",command=lambda: choise_cosmetic2(entries))


lbl.pack()
lbl0.pack()
combo.pack()
lbl1.pack()
combo2.pack()
ok.pack()

window.mainloop()