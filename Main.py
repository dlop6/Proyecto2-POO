import tkinter as Tk
from BaseDeDatosJSON import BaseDeDatosJSON
from ControladorUsuario import ControladorUsuario
from Aplicacion import Aplicacion

# Configuración de la ventana principal
filename = 'usuarios.json'
base_de_datos = BaseDeDatosJSON(filename)

root = Tk.Tk()
app = Aplicacion(root, base_de_datos)

# Ejecución de la aplicación
root.mainloop()
