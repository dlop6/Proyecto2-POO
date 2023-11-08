import sys
import os

# Add the root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as Tk
from Model.BaseDeDatosJSON import BaseDeDatosJSON
from Controller.ControladorUsuario import ControladorUsuario
from Controller.Aplicacion import Aplicacion

class Main:
    def __init__(self):
        filename = 'usuarios.json'
        base_de_datos = BaseDeDatosJSON(filename)

        root = Tk.Tk()
        app = Aplicacion(root, base_de_datos)
        root.mainloop()
