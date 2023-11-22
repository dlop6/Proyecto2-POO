'''
Universidad del Valle de Guatemala
Proyecto Final POO
Diego Lopez y Roberto Barreda - 23354
'''

import json
import uuid
from tkcalendar import Calendar
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from Orientacion import Orientacion
from News import News
from BaseDeDatosJSON import BaseDeDatosJSON
from Usuario import Usuario
from Cursos import Cursos

class Aplicacion(tk.Tk):
    def __init__(self, root, usuario=None):
        super().__init__(root)
        self.root = root
        self.usuario = usuario
        self.file_name = "usuarios.json"
        self.base_de_datos = BaseDeDatosJSON(self.file_name)
        self.controlador_usuario = Usuario(self.base_de_datos, "", "", "", False, "")
        self.news = News("pub_32493947bac2cd99a74d4b4821243a7ac98aa", self.root)
        self.root.geometry("400x300")
        self.root.title("Sistema de Autenticación")
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(expand=True, fill="both")
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

        if self.usuario:
            cursos_realizados = self.usuario.get("perfil", {}).get("Cursos realizados", [])

            if cursos_realizados:
                nombres_cursos = [curso["nombre"] for curso in cursos_realizados]

                self.label_curso = ctk.CTkLabel(self.root, text="Seleccione un curso:")
                self.label_curso.pack()

                self.selected_course_var = tk.StringVar()
                self.evaluar_curso_menu = tk.OptionMenu(self.root, self.selected_course_var, *nombres_cursos)
                self.evaluar_curso_menu.grid(row=4, column=1, padx=10, pady=10)

                self.label_rating = ctk.CTkLabel(self.root, text="Rating:")
                self.label_rating.pack()

                self.rating_slider = tk.Scale(self.root, from_=0, to=5, orient="horizontal", length=200, resolution=0.1)
                self.rating_slider.pack(pady=10)

                self.label_comentarios = ctk.CTkLabel(self.root, text="Comentarios:")
                self.label_comentarios.pack()
                self.entry_comentarios = ctk.CTkEntry(self.root)
                self.entry_comentarios.pack()

                self.boton_enviar_evaluacion = ctk.CTkButton(self.root, text="Enviar Evaluación", command=self.enviar_evaluacion_curso)
                self.boton_enviar_evaluacion.pack(pady=10)

                self.boton_exit = ctk.CTkButton(self.root, text="Exit", command=self.logged_menu)
                self.boton_exit.pack()
            else:
                self.label_no_courses = ctk.CTkLabel(self.root, text="No hay cursos completados para evaluar.")
                self.label_no_courses.pack(pady=10)
                self.boton_exit = ctk.CTkButton(self.root, text="Exit", command=self.logged_menu)
                self.boton_exit.pack()
        else:
            self.label_no_user = ctk.CTkLabel(self.root, text="No hay usuario registrado.")
            self.label_no_user.pack(pady=10)
            self.boton_exit = ctk.CTkButton(self.root, text="Exit", command=self.logged_menu)
            self.boton_exit.pack()


    def logged_menu(self):
       self.clear_screen()
       self.label_menu = ctk.CTkLabel(self.root, text="¡Bienvenido miembro de la comunidad de salud!")
       self.label_menu.pack(pady=10)
       button_texts = ["Noticias", "Cursos", "Agenda", "Evaluaciones", "Orientaciones", "Exit"]
       button_commands = [self.showNewsMenu, self.cursos, self.agenda, self.evaluar_curso, self.orientaciones, self.menu] 
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

        self.boton_crear_curso = ctk.CTkButton(self.root, text="Crear Curso", command=self.crear_curso_action)
        self.boton_crear_curso.pack(pady=10)

        self.boton_exit = ctk.CTkButton(self.root, text="Exit", command=self.logged_menu)
        self.boton_exit.pack()

    def crear_curso_action(self):
        nombre = self.entry_nombre.get()
        fecha = self.entry_fecha.get()
        cupo = self.entry_cupo.get()

        if nombre and fecha and cupo:
            curso = {"nombre": nombre, "fecha": fecha, "cupo": cupo}
            self.controlador_usuario.agregar_curso_usuario(curso)
            messagebox.showinfo("Curso Creado", f"Curso {nombre} creado exitosamente.")
            self.logged_menu()
        else:
            messagebox.showwarning("Datos Incompletos", "Por favor, complete todos los campos.")

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

    def eliminar_curso(self):
        nombre = self.entry_nombre.get()

        if nombre:
            curso = {"nombre": nombre}
            self.controlador_usuario.eliminar_curso(curso)
            messagebox.showinfo("Curso Eliminado", f"Curso {nombre} eliminado exitosamente.")
            self.logged_menu()
        else:
            messagebox.showwarning("Datos Incompletos", "Por favor, complete todos los campos.")

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
            event_id = str(uuid.uuid4())

            event = {"id": event_id, "date": selected_date, "description": event_description}
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
            Usuario.agregar_evaluacion_curso(Cursos["nombre"], rating, comentarios)
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

    def orientaciones(self):
        self.clear_screen()
        self.label_orientaciones = ctk.CTkLabel(self.root, text="Orientaciones y Ratings de Cursos")
        self.label_orientaciones.pack(pady=10)

        orientacion = Orientacion(self.root, "usuarios.json")
        orientacion.mostrar_orientacion()

        self.boton_exit = ctk.CTkButton(self.root, text="Exit", command=self.logged_menu)
        self.boton_exit.pack()

def main():
    root = ctk.CTk()
    root.configure(bg='black')
    app = Aplicacion(root)
    root.mainloop()

if __name__ == "__main__":
    main()