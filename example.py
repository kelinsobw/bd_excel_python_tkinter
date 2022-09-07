import tkinter
root = tkinter.Tk()

canvas = tkinter.Canvas(root, borderwidth=0, background="#ffffff")
frame= tkinter.Frame(canvas, background="#ffffff")
vsb = tkinter.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4, 4), window=frame, anchor="nw")

for i in range(20):
    lbl = tkinter.Label(frame, text=f"Label {i}")
    lbl.pack(side="top")

canvas.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"))

root.mainloop()