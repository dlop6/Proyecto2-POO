'''
Universidad del Valle de Guatemala
Proyecto Final POO
Roberto Barreda - 23354
prueba
'''

import json
from tkcalendar import Calendar
import tkinter as tk
from tkinter import messagebox, ttk
from Usuario import Usuario
import customtkinter as ctk
from customtkinter import *
from BaseDeDatosJSON import BaseDeDatosJSON
from Usuario import Usuario
from News import News
from Cursos import Cursos

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.file_name = "usuarios.json"
        self.base_de_datos = BaseDeDatosJSON(self.file_name)
        self.controlador_usuario = Usuario(self.base_de_datos, "", "", "", False, "")
        self.news = News("pub_32493947bac2cd99a74d4b4821243a7ac98aa", self.root)
        self.logged_user = {}
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

        self.code_label = ctk.CTkLabel(self.root, text="Nombre:")
        self.code_label.pack()
        self.entry_code = ctk.CTkEntry(self.root)
        self.entry_code.pack()

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
        nombre = self.entry_code.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        es_miembro_salud = self.var_miembro_salud.get()
        carnet_colegiado = self.entry_carnet.get()

        resultado = self.base_de_datos.crear_cuenta(email, password, nombre, carnet_colegiado, es_miembro_salud)

        if resultado:
            messagebox.showinfo("Resultado del Registro", "¡Usuario registrado exitosamente!")
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
            self.logged_user = self.base_de_datos.buscar_usuario(email)
            self.logged_menu()
        else:
            messagebox.showinfo("No se pudo iniciar sesión", "El correo electrónico o la contraseña son incorrectos")
    def agenda(self):
        self.clear_screen()
        self.label_agenda = ctk.CTkLabel(self.root, text="Agenda")
        self.label_agenda.pack(pady=10)

        self.label_date = ctk.CTkLabel(self.root, text="Seleccionar Fecha:")
        self.label_date.pack()
        self.calendar = Calendar(self.root, selectmode="day", year=2023, month=11, day=7)
        self.calendar.pack(pady=10)

        self.label_event = ctk.CTkLabel(self.root, text="Descripción del Evento:")
        self.label_event.pack()
        self.entry_event = ctk.CTkEntry(self.root)
        self.entry_event.pack()

        self.button_agendar = ctk.CTkButton(self.root, text="Agendar", command=self.agendar_evento)
        self.button_agendar.pack(pady=10)

        self.button_exit = ctk.CTkButton(self.root, text="Exit", command=self.logged_menu)
        self.button_exit.pack()
    
    def evaluar_curso(self):
        self.clear_screen()
        self.label_evaluacion_curso = ctk.CTkLabel(self.root, text="Evaluación de Curso")
        self.label_evaluacion_curso.pack(pady=10)

        cursos_disponibles = ["Curso 1", "Curso 2", "Curso 3"]

        self.label_curso = ctk.CTkLabel(self.root, text="Seleccione un curso:")
        self.label_curso.pack()

        self.selected_course_var = tk.StringVar()
        self.combobox_curso = ttk.Combobox(self.root, textvariable=self.selected_course_var, values=cursos_disponibles)
        self.combobox_curso.pack(pady=10)

        self.label_rating = ctk.CTkLabel(self.root, text="Rating:")
        self.label_rating.pack()
        self.entry_rating = ctk.CTkEntry(self.root)
        self.entry_rating.pack()

        self.label_comentarios = ctk.CTkLabel(self.root, text="Comentarios:")
        self.label_comentarios.pack()
        self.entry_comentarios = ctk.CTkEntry(self.root)
        self.entry_comentarios.pack()

        self.boton_enviar_evaluacion = ctk.CTkButton(self.root, text="Enviar Evaluación", command=self.enviar_evaluacion_curso)
        self.boton_enviar_evaluacion.pack(pady=10)

        self.boton_exit = ctk.CTkButton(self.root, text="Exit", command=self.logged_menu)
        self.boton_exit.pack()

    def logged_menu(self):
       self.clear_screen()
       self.label_menu = ctk.CTkLabel(self.root, text="¡Bienvenido miembro de la comunidad de salud!")
       self.label_menu.pack(pady=10)
       button_texts = ["Noticias", "Cursos", "Agenda", "Evaluaciones", "Orientaciones", "Exit"]
       button_commands = [self.showNewsMenu, self.cursos, self.agenda, self.evaluar_curso, None, self.menu] 
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
        self.cursos = Cursos(self.logged_user, self.root)
        self.label_menu = ctk.CTkLabel(self.root, text="Crear Curso")
        self.label_menu.pack(pady=10)
        
        self.label_codigo = ctk.CTkLabel(self.root, text="Código:")
        self.label_codigo.pack()
        self.entry_codigo = ctk.CTkEntry(self.root)
        self.entry_codigo.pack()

        self.code_label = ctk.CTkLabel(self.root, text="Nombre:")
        self.code_label.pack()
        self.entry_code = ctk.CTkEntry(self.root)
        self.entry_code.pack()

        self.label_fecha = ctk.CTkLabel(self.root, text="Fecha:")
        self.label_fecha.pack()
        self.entry_fecha = ctk.CTkEntry(self.root)
        self.entry_fecha.pack()

        self.label_localidad = ctk.CTkLabel(self.root, text="Localidad:")
        self.label_localidad.pack()
        self.entry_localidad = ctk.CTkEntry(self.root)
        self.entry_localidad.pack()
        

        self.boton_crear_curso = ctk.CTkButton(
            self.root, 
            text="Crear Curso", 
            command=lambda: self.cursos.agregar_curso({
            "codigo": self.entry_codigo.get(),
            "nombre": self.entry_code.get(),
            "fecha": self.entry_fecha.get(),
            "certificado": False,
            "localidad": self.entry_localidad.get()
         })
        )
        self.boton_crear_curso.pack(pady=10)


        self.boton_exit = ctk.CTkButton(self.root, text="Exit", command=self.logged_menu)
        self.boton_exit.pack()

    def eliminar_curso(self):
        self.cursos = Cursos(self.logged_user, self.root)
        self.clear_screen()
        self.label_menu = ctk.CTkLabel(self.root, text="Eliminar Curso")
        self.label_menu.pack(pady=10)

        self.code_label = ctk.CTkLabel(self.root, text="Codigo de curso:")
        self.code_label.pack()
        self.entry_code = ctk.CTkEntry(self.root)
        self.entry_code.pack()

        self.boton_eliminar_curso = ctk.CTkButton(self.root, text="Eliminar Curso", command= lambda: self.cursos.eliminar_curso(self.entry_code.get()))
        self.boton_eliminar_curso.pack(pady=10)

        self.boton_exit = ctk.CTkButton(self.root, text="Exit", command=self.logged_menu)
        self.boton_exit.pack()

    def agendar_evento(self):
        self.clear_screen()
        self.label_agenda = ctk.CTkLabel(self.root, text="Agenda")
        self.label_agenda.pack(pady=10)

        self.label_date = ctk.CTkLabel(self.root, text="Seleccionar Fecha:")
        self.label_date.pack()
        self.calendar = Calendar(self.root, selectmode="day", year=2023, month=11, day=7)
        self.calendar.pack(pady=10)

        self.label_event = ctk.CTkLabel(self.root, text="Descripción del Evento:")
        self.label_event.pack()
        self.entry_event = ctk.CTkEntry(self.root)
        self.entry_event.pack()

        self.button_agendar = ctk.CTkButton(self.root, text="Agendar", command=self.agendar_evento)
        self.button_agendar.pack(pady=10)

        self.button_exit = ctk.CTkButton(self.root, text="Exit", command=self.logged_menu)
        self.button_exit.pack()

    def agendar_evento(self):
        selected_date = self.calendar.get_date()
        event_description = self.entry_event.get()

        if selected_date and event_description:
            # Guardar eventos (esto es solo un ejemplo, debes adaptarlo a tu lógica)
            event = {"date": selected_date, "description": event_description}
            events = []

            try:
                with open('events.json', 'r') as json_file:
                    events = json.load(json_file)
            except FileNotFoundError:
                pass

            events.append(event)

            with open('events.json', 'w') as json_file:
                json.dump(events, json_file)

            messagebox.showinfo("Evento Agendado", "Evento agendado exitosamente.")
            self.logged_menu()
        else:
            messagebox.showwarning("Datos Incompletos", "Por favor, complete todos los campos.")
    
    def enviar_evaluacion_curso(self):
        selected_course = self.selected_course_var.get()
        rating = self.entry_rating.get()
        comentarios = self.entry_comentarios.get()

        if selected_course and rating and comentarios:
            self.controlador_usuario.agregar_evaluacion_curso(selected_course, rating, comentarios)
            messagebox.showinfo("Evaluación Enviada", "Evaluación de curso enviada exitosamente.")
            self.logged_menu()
        else:
            messagebox.showwarning("Datos Incompletos", "Por favor, complete todos los campos.")
        
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