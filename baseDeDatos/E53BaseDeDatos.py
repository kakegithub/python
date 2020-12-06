
import sqlite3
from sqlite3.dbapi2 import Cursor

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

# Lectura de datos
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confeccion'")

productos=miCursor.fetchall()
print(productos)

# Actualizacion de datos
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'" )

# Borrar registros
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")



miConexion.commit()

miConexion.close()
