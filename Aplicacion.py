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
from ControladorUsuario import ControladorUsuario

class Aplicacion:
    def __init__(self, root, base_de_datos):
        self.root = root
        self.base_de_datos = base_de_datos
        self.controlador_usuario = ControladorUsuario(self.base_de_datos)
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

        resultado = self.controlador_usuario.crear_cuenta(nombre, email, password, es_miembro_salud, carnet_colegiado)
        messagebox.showinfo("Resultado del Registro", resultado)

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

        resultado = self.controlador_usuario.autenticar(email, password)
        messagebox.showinfo("Resultado del Inicio de Sesión", resultado)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    filename = 'usuarios.json'
    base_de_datos = BaseDeDatosJSON(filename)
    root = ctk.CTk()
    root.configure(bg='black')
    app = Aplicacion(root, base_de_datos)
    root.mainloop()

if __name__ == "__main__":
    main()