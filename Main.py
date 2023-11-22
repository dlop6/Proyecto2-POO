import customtkinter as ctk
from BaseDeDatosJSON import BaseDeDatosJSON
from AppController import Aplicacion
from Cursos import Cursos
from Usuario import Usuario

class Main:
    def __init__(self, filename):
        self.filename = filename
        self.base_de_datos = BaseDeDatosJSON(self.filename)
        self.usuario_actual = None

    def run(self):
        base_de_datos = BaseDeDatosJSON(self.filename)
        usuario_actual = None
        cursos = Cursos()
        root = ctk.CTk()
        app = Aplicacion(root, self.usuario_actual)

        def open_cursos_menu():
            if usuario_actual:
                cursos.cursos_menu(usuario_actual)

        button_ver_cursos = ctk.CTkButton(root, text="Ver Cursos", command=open_cursos_menu)
        if usuario_actual:
            button_ver_cursos.pack()

        root.mainloop()

if __name__ == '__main__':
    filename = 'usuarios.json'
    main = Main(filename)
    main.run()

