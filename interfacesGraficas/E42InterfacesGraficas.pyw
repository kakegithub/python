# Cuadros de texto--->Entry
from tkinter import *

raiz = Tk()

miFrame=Frame(raiz, width="1200", height="600")

miFrame.pack()

# Variables
miNombre = StringVar()

cuadroNombre = Entry(miFrame, textvariable=miNombre )
# Metodo grid(row,column)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify=LEFT)

cuadroPass = Entry(miFrame, )
cuadroPass.grid(row=1, column=1, padx=10, pady=10) 
cuadroPass.config(show="*", fg="black", justify=LEFT)


cuadroApellidos = Entry(miFrame, )
cuadroApellidos.grid(row=2, column=1, padx=10, pady=10) 
cuadroApellidos.config(fg="red", justify=LEFT)

cuadroDireccion = Entry(miFrame, )
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10) 
cuadroDireccion.config(fg="red", justify=LEFT)


# Tipo texto
textoComentarios=Text(miFrame, width=16, height=5)
textoComentarios.grid(row=4, column=1, padx=10, pady=10)
textoComentarios=Text(fg="red")

# Vamos a añadirle un objeto de tipo scrollbar a textoComentarios y decirle que es vertical
scrollVert=Scrollbar(miFrame, command=textoComentarios.yview)
# Ahora lo colocamos y lo adaptamos al tamaño de textoComentarios
scrollVert.grid(row=4, column=2, sticky="nsew")
# Ponemos el posicionador del texto corectamente
textoComentarios.config(yscrollcommand=scrollVert.set)


nombreLabel=Label(miFrame, text="Nombre:") 
# La propiedad sticky nos alinea el componente(coordenadas cardinales)
# La propiedad padding nos sirve para separar elementos del contenido(padx, pady)
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Pasword:")
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidosLabel=Label(miFrame, text="Apellidos:")
apellidosLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

# Añadimos un boton y le asignamos un comportamiento
def codigoBoton():
    miNombre.set("Juan")


botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()