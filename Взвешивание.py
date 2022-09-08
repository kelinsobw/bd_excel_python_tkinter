import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox


from main import return_row, new_cosmetic, add_cosmetic, return_cabinet, return_cabitet_cosmetic, save_in_file


def save(entries, name, meaning):
    meaning_now = []
    for item in entries:
        meaning_now.append(item.get())
    print(str(combo.get()))
    save_in_file(name, meaning, meaning_now, str(combo2.get()), str(combo.get()))


def delete_cosmetic(entries):
    for item in entries:
        item.destroy()

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
            label=Label(frame, text=item, anchor='w')
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
    entries.append(save_bt)
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))


window = Tk()
window.title("Взвешивание")
window.geometry('1600x800')

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

lbl.pack()
lbl0.pack()
combo.pack()
lbl1.pack()
combo2.pack()
ok.pack()
replay.pack()

window.mainloop()
