# Importacion de clases
from sqlite3.dbapi2 import connect
from tkinter import *
from tkinter import messagebox
import sqlite3

#--------------------Funciones--------------------------------------

def conexionBBDD():
    
    miConexion=sqlite3.connect("Usuarios")
    
    miCursor=miConexion.cursor()

    try:
        
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_USUARIO VARCHAR(50),
                PASSWORD VARCHAR(50),
                APELLIDO VARCHAR(10),
                DIRECCION VARCHAR(50),
                COMENTARIOS VARCHAR(100)
                )
        ''')
        
        messagebox.showinfo("BBDD", "BBDD creada con exito")
    
    except:
        
        messagebox.showwarning("¡Atencion!", "La BBDD ya existe")


# Creamos la ventana
root = Tk()

# Creacion del menu
barraMenu=Menu(root)

#Configuramos el menu
root.config(menu=barraMenu, width=300, height=300)

# Creacion de los elementos bbddMenu
bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir")

# Creacion de los elementos borrarMenu
borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos")

# Creacion de los elementos crudMenu
crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear")
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

#Creacion de los elementos ayudaMenu
ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

# Agrgamos los elementos a barraMenu
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


#-----------comienzo de campos------------------------
miFrame = Frame(root)
miFrame.pack()

cuadroID=Entry(miFrame)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify=RIGHT)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*", justify=RIGHT)


cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)

scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

# Activamos el scroll
scrollVert.activate=True

#---------------------Label-------------------------------
idLabel=Label(miFrame, text="Id:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Password:")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#--------------------Botones------------------------------------------
miFrame2=Frame(root) #Usamos otro frame para los botones
miFrame2.pack()

botonCrear=Button(miFrame2, text="Create")
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Read")
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Update")
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Delete")
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)


root.mainloop()