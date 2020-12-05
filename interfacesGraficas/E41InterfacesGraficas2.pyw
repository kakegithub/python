
# Creacion de un label
# variableLabel = Label(contenedor,opciones)

from tkinter import *

root=Tk()

miFrame=Frame(root, width="500", height="400")

miFrame.pack()

# Forma abreviada
#Label(miFrame, text="Hola alumnos de python").place(x=100, y=200)


miLabel = Label(miFrame, text="Hola alumnos de python", fg="red", font=("Comic Sans MS", 18))
#miLabel.pack()
miLabel.place(x=100, y=200) # Usamos el metodo place() para situar el Label en vez de pack()

# TKinter trabaja con imagenes png y gif
try:
   miImagen=PhotoImage(file=".\interfacesGraficas\imagenes\Tux.png")
   print("entra 1")
except TclError:
   miImagen=PhotoImage(file=".\imagenes\Tux.png")
   print("entra")

miLabel2 = Label(miFrame, image=miImagen)

miLabel2.place(x=100, y=250)

root.mainloop()
