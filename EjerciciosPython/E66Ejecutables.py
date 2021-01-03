# Creacion de ejecutables
# Desde el terminal ejecutamos: pip install pyinstaller
# Nos movemos al directorio del archivo del que queremos hacer el ejecutable desde el terminal
# Ejecutamos en el terminal: pyinstaller nombreArchivo.py

# En la carpeta dist esta la aplicacion para distribuirla

# Si queremos ocultar la consola
# Ejecutamos en el terminal: pyinstaller --windowed nombreArchivo.py

# Si queremos que todo se meta en un unico archivo
# Ejecutamos en el terminal: pyinstaller --windowed --onefile nombreArchivo.py

# Si queremos poner un icono
# Ejecutamos en el terminal: pyinstaller --windowed --onefile --icon=./icono.ico nombreArchivo.py