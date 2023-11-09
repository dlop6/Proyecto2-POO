import customtkinter as ctk
from BaseDeDatosJSON import BaseDeDatosJSON
from AppController import Aplicacion

class Main:
    def __init__(self, filename):
        self.filename = filename

    def run(self):
        base_de_datos = BaseDeDatosJSON(self.filename)

        root = ctk.CTk()

        app = Aplicacion(root)

        root.mainloop()

if __name__ == '__main__':
    filename = 'usuarios.json'
    main = Main(filename)
    main.run()
