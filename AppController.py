'''
Universidad del Valle de Guatemala
Proyecto Final POO
Roberto Barreda - 23354
'''

import tkinter as tk
from tkinter import messagebox
from Usuario import Usuario
import customtkinter as ctk

from BaseDeDatosJSON import BaseDeDatosJSON
from Usuario import Usuario
from News import News

class Aplicacion:
    def __init__(self, root):
        self.root = root
        
        self.file_name = "usuarios.json"
        self.base_de_datos = BaseDeDatosJSON(self.file_name)
        self.controlador_usuario = Usuario(self.base_de_datos, "", "", "", False, "")
        self.news = News("pub_32493947bac2cd99a74d4b4821243a7ac98aa", self.root)
        self.root.geometry("400x300")
        self.root.title("Sistema de Autenticación")

        self.menu()
    
    def menu(self):
        self.clear_screen()
        self.root.geometry("400x300")
        self.label_menu = ctk.CTkLabel(self.root, text="Menú Principal")
        self.label_menu.pack(pady=10)

        self.boton_signup = ctk.CTkButton(self.root, text="Sign Up", command=self.signup)
        self.boton_signup.pack(pady=5)

        self.boton_login = ctk.CTkButton(self.root, text="Log In", command=self.login)
        self.boton_login.pack(pady=5)

        self.boton_exit = ctk.CTkButton(self.root, text="Exit", command=self.root.quit)
        self.boton_exit.pack(pady=5)

    def signup(self):
        self.clear_screen()
        self.root.geometry("400x500")
        self.label_registro = ctk.CTkLabel(self.root, text="Registro de Usuario")
        self.label_registro.pack(pady=10)

        self.label_nombre = ctk.CTkLabel(self.root, text="Nombre:")
        self.label_nombre.pack()
        self.entry_nombre = ctk.CTkEntry(self.root)
        self.entry_nombre.pack()

        self.label_email = ctk.CTkLabel(self.root, text="Correo Electrónico:")
        self.label_email.pack()
        self.entry_email = ctk.CTkEntry(self.root)
        self.entry_email.pack()

        self.label_password = ctk.CTkLabel(self.root, text="Contraseña:")
        self.label_password.pack()
        self.label_password.pack()
        self.entry_password = ctk.CTkEntry(self.root, show="*")
        self.entry_password.pack()

        self.label_miembro_salud = ctk.CTkLabel(self.root, text="¿Es miembro del cuerpo de salud?")
        self.label_miembro_salud.pack()
        self.var_miembro_salud = tk.BooleanVar()
        self.checkbox_miembro_salud = ctk.CTkCheckBox(self.root, text="Sí", variable=self.var_miembro_salud)
        self.checkbox_miembro_salud.pack()

        self.label_carnet = ctk.CTkLabel(self.root, text="Número de carné (si aplica):")
        self.label_carnet.pack()
        self.entry_carnet = ctk.CTkEntry(self.root)
        self.entry_carnet.pack()

        self.boton_registro = ctk.CTkButton(self.root, text="Registrarse", command=self.registrarse)
        self.boton_registro.pack(pady=10)

        self.boton_exit = ctk.CTkButton(self.root, text="Exit", command=self.menu)
        self.boton_exit.pack()

    def registrarse(self):
        nombre = self.entry_nombre.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        es_miembro_salud = self.var_miembro_salud.get()
        carnet_colegiado = self.entry_carnet.get()

        resultado = self.base_de_datos.crear_cuenta(email, password, nombre, carnet_colegiado, es_miembro_salud)
        
        if resultado: 
            messagebox.showinfo("Resultado del Registro", "¡Usuario registra2do exitosamente!")
            self.menu()
        else:
            messagebox.showinfo("Resultado del Registro", "El correo electrónico ya está registrado")

    def login(self):
        self.clear_screen()
        self.label_inicio_sesion = ctk.CTkLabel(self.root, text="Iniciar Sesión")
        self.label_inicio_sesion.pack(pady=10)

        self.label_email_inicio = ctk.CTkLabel(self.root, text="Correo Electrónico:")
        self.label_email_inicio.pack()
        self.entry_email_inicio = ctk.CTkEntry(self.root)
        self.entry_email_inicio.pack()

        self.label_password_inicio = ctk.CTkLabel(self.root, text="Contraseña:")
        self.label_password_inicio.pack()
        self.entry_password_inicio = ctk.CTkEntry(self.root, show="*")
        self.entry_password_inicio.pack()

        self.boton_inicio_sesion = ctk.CTkButton(self.root, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.boton_inicio_sesion.pack(pady=10)

        self.boton_exit = ctk.CTkButton(self.root, text="Exit", command=self.menu)
        self.boton_exit.pack()


    def iniciar_sesion(self):
        email = self.entry_email_inicio.get()
        password = self.entry_password_inicio.get()

        resultado = self.base_de_datos.autenticar(email, password)
        if resultado:
            self.logged_menu()
        else:
            messagebox.showinfo("No se pudo iniciar sesión", "El correo electrónico o la contraseña son incorrectos")
        

    def logged_menu(self):
       self.clear_screen()
       self.label_menu = ctk.CTkLabel(self.root, text="¡Bienvenido miembro de la comunidad de salud!")
       self.label_menu.pack(pady=10)
       button_texts = ["Noticias", "Cursos", "Agenda", "Evaluaciones", "Orientaciones", "Exit"]
       button_commands = [self.showNewsMenu, self.cursos, None, None, None, self.menu] 
       for text, command in zip(button_texts, button_commands):
           button = ctk.CTkButton(self.root, text=text, command=command)
           button.pack(pady=5)
           
    def cursos(self):
        self.clear_screen()
        self.label_menu = ctk.CTkLabel(self.root, text="Cursos")
        self.label_menu.pack(pady=10)
        button_texts = ["Asignar Curso", "Eliminar Curso", "Exit"]
        button_commands = [self.crear_curso, self.eliminar_curso, self.logged_menu] 
        for text, command in zip(button_texts, button_commands):
            button = ctk.CTkButton(self.root, text=text, command=command)
            button.pack(pady=5)
        
    def crear_curso(self):
        self.clear_screen()
        self.label_menu = ctk.CTkLabel(self.root, text="Crear Curso")
        self.label_menu.pack(pady=10)

        self.label_nombre = ctk.CTkLabel(self.root, text="Nombre:")
        self.label_nombre.pack()
        self.entry_nombre = ctk.CTkEntry(self.root)
        self.entry_nombre.pack()

        self.label_fecha = ctk.CTkLabel(self.root, text="Fecha:")
        self.label_fecha.pack()
        self.entry_fecha = ctk.CTkEntry(self.root)
        self.entry_fecha.pack()

        self.label_cupo = ctk.CTkLabel(self.root, text="Cupo:")
        self.label_cupo.pack()
        self.entry_cupo = ctk.CTkEntry(self.root)
        self.entry_cupo.pack()

        self.boton_crear_curso = ctk.CTkButton(self.root, text="Crear Curso", command=self.crear_curso)
        self.boton_crear_curso.pack(pady=10)

        self.boton_exit = ctk.CTkButton(self.root, text="Exit", command=self.logged_menu)
        self.boton_exit.pack()

    def eliminar_curso(self):
        self.clear_screen()
        self.label_menu = ctk.CTkLabel(self.root, text="Eliminar Curso")
        self.label_menu.pack(pady=10)

        self.label_nombre = ctk.CTkLabel(self.root, text="Nombre:")
        self.label_nombre.pack()
        self.entry_nombre = ctk.CTkEntry(self.root)
        self.entry_nombre.pack()

        self.boton_eliminar_curso = ctk.CTkButton(self.root, text="Eliminar Curso", command=self.eliminar_curso)
        self.boton_eliminar_curso.pack(pady=10)

        self.boton_exit = ctk.CTkButton(self.root, text="Exit", command=self.logged_menu)
        self.boton_exit.pack()
        
    def showNewsMenu(self):
        self.clear_screen()
        self.news.news_menu()
        
        self.root.exit_button = ctk.CTkButton(self.root, text="Exit", command=self.logged_menu)
        self.root.exit_button.pack(pady=10)
        
        self.root.mainloop()
        pass


    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    root = ctk.CTk()
    root.configure(bg='black')
    app = Aplicacion(root)
    root.mainloop()

if __name__ == "__main__":
    main()