from tkinter import *

rows = []
for i in range(2):
    cols = []
    for j in range(4):
        e = Entry(relief=RIDGE)
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, '%d.%d' % (i, j))


'''def onPress():
    for row in rows:
        for col in row:
            pass'''
#Button(text='Fetch', command=onPress).grid()
mainloop()