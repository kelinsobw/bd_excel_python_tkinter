from tkinter import *



root = Tk()

height = 5
width = 5
cells = {}
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Entry(root)
        b.insert(0,"2")
        b.grid(row=i, column=j)
        cells[(i,j)] = b

mainloop()