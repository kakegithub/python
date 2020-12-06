# Base de datos

# Importamos sqlite3
import sqlite3


# Abrir y crear conexion
miConexion=sqlite3.connect("PrimeraBase")

# Creamos el puntero
miCursor=miConexion.cursor()

# Ejecutamos la consulta SQL
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")

# Creamos una tupla para insertar varios productos a la vez
variosProductos=[
    ("Jarron",90,"Ceramica"),
    ("Camion",20,"Jugueteria")
    ]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

# Acceder a la informacion
miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos = miCursor.fetchall()
#print(variosProductos)

#for producto in variosProductos:
#    print(producto)

for producto in variosProductos:
    print("Nombre articulo: ", producto[0], " Seccion ", producto[2])

miConexion.commit()


#Cerramos el puntero


# Cerramos la conexion
miConexion.close()