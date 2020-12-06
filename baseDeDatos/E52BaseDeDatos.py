# Clausula UNIQUE

import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

miCursor.execute('''
    CREATE TABLE PRODUCTOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
        PRECIO INTEGER,
        SECCION VARCHAR(20)
    )
''')

productos=[

    ("pelota", 20, "jugueteria"),
    ("pantalon", 15, "confeccion"),
    ("destornillador", 25, "ferreteria"),
    ("jarron", 45, "ceramica")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL, ?, ?, ?)", productos) # NULL lo reserva para el campo ID

miConexion.commit()


miConexion.close()
