from tkinter import *
from tkinter.ttk import Combobox

from main import return_row, new_cosmetic, add_cosmetic, return_cabinet, return_cabitet_cosmetic, save_in_file


def save(entries, name, meaning):
    meaning_now = []
    for item in entries:
        meaning_now.append(item.get())
    save_in_file(name, meaning, meaning_now, str(combo2.get()), str(combo.get()))


def delete_cosmetic(entries):
    for item in entries:
        item.destroy()

def choise_cosmetic(entries):
    cosmitin_cab = return_cabitet_cosmetic(combo2.get())
    name = []
    meaning = []
    i = 7
    for item in cosmitin_cab:
        label=Label(text=item)
        label.grid(row=i, column=0)
        entries.append((label))
        name.append(item)
        entry = Entry(width=10)
        entry.insert(0, cosmitin_cab.get(item))
        meaning.append(cosmitin_cab.get(item))
        entry.grid(row=i, column=1)
        entries.append(entry)
        i = i+1
    save_bt = Button(window, text="Сохранить", command=lambda: save(entries, name, meaning))
    save_bt.grid()
    entries.append(save_bt)


window = Tk()
window.title("Взвешивание")
window.geometry('400x500')

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
ok = Button(window, text="Вывести косметику",command=lambda: choise_cosmetic(entries))
replay = Button(window, text="Далее", command=lambda: delete_cosmetic(entries))

lbl.grid()
lbl0.grid()
combo.grid()
lbl1.grid()
combo2.grid()
ok.grid()
replay.grid()

window.mainloop()
