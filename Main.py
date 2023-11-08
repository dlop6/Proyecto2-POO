


'''
Universidad del Valle de Guatemala
Proyecto Final POO
Roberto Barreda - 23354
'''
#No funciona en las carpetas
import tkinter as Tk
import customtkinter as ctk
from BaseDeDatosJSON import BaseDeDatosJSON
from AppController import Aplicacion

# Configuración de la ventana principal
filename = 'usuarios.json'
base_de_datos = BaseDeDatosJSON(filename)

root = ctk.CTk()

app = Aplicacion(root)

# Ejecución de la aplicación
root.mainloop()

# Directorio.Archivo

#from Directorio.Archivo import Directorio.Archivo
#import Directorio.Archivo as "Algo"