# checkbuttons

from tkinter import *
import tkinter

root=Tk()
root.title("Ejemplo")

playa=IntVar()
montagna=IntVar()
turismoRural=IntVar()

def opcionesViaje():
    opcionEscogida=""
    if (playa.get()==1):
        opcionEscogida+=" playa"
    if (montagna.get()==1):
        opcionEscogida+=" montaña"
    if (turismoRural.get()==1):
        opcionEscogida+=" turismoRural"

    textoFinal.config(text=opcionEscogida)


try:
    foto=PhotoImage(file=".\interfacesGraficas\imagenes\Tux.png")
    Label(root, image=foto).pack()
except TclError:
    foto=PhotoImage(file=".\imagenes\Tux.png")
    Label(root, image=foto).pack()


frame=Frame(root)
frame.pack()
Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montagna, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()


root.mainloop()