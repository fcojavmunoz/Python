from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")

ventana = Tk()
opcion = StringVar()
opcion.set(None)

label = Label(text="¿A qué hora le viene bien que entreguemos su pedido?")
label.pack()
Radiobutton(ventana, text="De 8:00 a 10:00", variable=opcion,
            value='De 8:00 a 10:00', command=seleccionar).pack(anchor=W)
Radiobutton(ventana, text="De 10:00 a 14:00", variable=opcion,
            value='De 10:00 a 14:00', command=seleccionar).pack(anchor=W)
Radiobutton(ventana, text="De 16:00 a 19:00", variable=opcion,
            value='De 16:00 a 19:00', command=seleccionar).pack(anchor=W)
Radiobutton(ventana, text="De 19:00 a 21:00", variable=opcion,
            value='De 19:00 a 21:00', command=seleccionar).pack(anchor=W)

monitor = Label(ventana)
monitor.pack()
Button(ventana, text="Reset", command=reset).pack()

ventana.mainloop()