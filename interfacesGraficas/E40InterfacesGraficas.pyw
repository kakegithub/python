# Raiz tk

from tkinter import *
# Construyendo la Ventana
raiz = Tk()
raiz.title("Ventana de pruebas") # Poniendo titulo
raiz.resizable(True, True) # Redimensionar o no la ventana
try:
   raiz.iconbitmap("./interfacesGraficas/iconos/tux.ico") # Cambiamos el icono
except TclError:    
    raiz.iconbitmap("./iconos/tux.ico") # Para que busca en esta ruta si no lo encuentra en la otra

#raiz.geometry("650x350") # Cambia el tamaño de la ventana
raiz.config(bg="blue")

# Construyendo el Frame
# Todo lo que aplicamos al Frame se lo podemos aplicar tambien a la raiz
miFrame = Frame()
#miFrame.pack(side="right", anchor="s") # Metemos el Frame en la ventana y lo posicionamos
#miFrame.pack(fill="x") # Expande horizontalmente
#miFrame.pack(fill="y", expand=True) # Expande verticalmente
miFrame.pack(fill="both", expand=True) # Expande en ambas direcciones
miFrame.config(bg="red") # Damos color al Frame
miFrame.config(width="650", height="350")
miFrame.config(bd=35)# Cambiamos el tamaño del borde
miFrame.config(relief="groove") # Cambiamos el tipo de borde
miFrame.config(cursor="pirate") # Cambiamos el cursor



raiz.mainloop()



