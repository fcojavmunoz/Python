from tkinter import *
master = Tk()
elemento = StringVar()
listbox = Listbox(master)
for item in ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4", "Elemento 5", "Elemento 6", "Elemento 7", "Elemento 8", "Elemento 9", "Elemento 10"]:
 listbox.insert(END, item)
listbox.pack()
label = Label(text="Elementos elementales")
label.pack()
master.mainloop()