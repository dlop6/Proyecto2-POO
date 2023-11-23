from Usuario import Usuario
from BaseDeDatosJSON import BaseDeDatosJSON
from ScreenController import ScreenController
import customtkinter as ctk
from tkinter import messagebox
import json



class Administrador():
    def __init__(self,  root):
        self.admin_email = "admin@gmail.com"
        self.admin_password = "admin"
        self.root = root
        self.screen_controller = ScreenController(self.root)
        
    def admin_login_menu(self):
        self.screen_controller.clear_screen()
        self.root.title("Administrador")
        self.root.geometry("500x500")
        self.root.resizable(True, True)
        
        self.root.admin_login_label = ctk.CTkLabel(self.root, text="Ingrese su correo y contraseña para ingresar como administrador")
        self.root.admin_login_label.pack(pady = 5)
        
        self.root.admin_email_label = ctk.CTkLabel(self.root, text="Correo")
        self.root.admin_email_label.pack(pady = 5)
        
        self.root.admin_email_entry = ctk.CTkEntry(self.root)
        self.root.admin_email_entry.pack(pady = 5)
        
        self.root.admin_password_label = ctk.CTkLabel(self.root, text="Contraseña")
        self.root.admin_password_label.pack(pady = 5)
        
        self.root.admin_password_entry = ctk.CTkEntry(self.root)
        self.root.admin_password_entry.pack(pady = 5)
        
        self.root.admin_login_button = ctk.CTkButton(self.root, text="Ingresar", command= lambda: self.admin_menu(self.root.admin_email_entry.get(), self.root.admin_password_entry.get()))
        self.root.admin_login_button.pack(pady = 5)
    
    def admin_menu(self, email, password):
        
        if email == self.admin_email and password == self.admin_password:
            self.screen_controller.clear_screen()
            self.root.title("Administrador")
            self.root.geometry("500x500")
            self.root.resizable(True, True)
            
            self.root.delete_user_button = ctk.CTkButton(self.root, text="Eliminar usuario", command=self.delete_user_menu)
            self.root.delete_user_button.pack(pady = 5)
            
            self.root.curso_certificado = ctk.CTkButton(self.root, text="Cambiar estado de certificado a un curso", command=self.change_certificado_menu)
            self.root.curso_certificado.pack(pady = 5)
        else:
            messagebox.showerror("Error", "Correo o contraseña incorrectos")
            

    
    def delete_user_menu(self):
        self.screen_controller.clear_screen()
        self.root.title("Eliminar usuario")
        self.root.geometry("500x500")
        self.root.resizable(True, True)


        self.root.delete_user_label = ctk.CTkLabel(self.root, text="Ingrese el correo del usuario que desea eliminar")
        self.root.delete_user_label.pack(pady = 5)

        self.root.delete_user_entry = ctk.CTkEntry(self.root)
        self.root.delete_user_entry.pack(pady = 5)
        
        self.user_to_delete = self.root.delete_user_entry.get()

        self.root.delete_user_button = ctk.CTkButton(self.root, text="Eliminar usuario", command= lambda: self.delete_user(self.user_to_delete))
        self.root.delete_user_button.pack(pady = 5)
    
    def delete_user(self, user_to_delete):
        with open("usuarios.json", "r") as file:
            users = json.load(file)
        
        updated_users = [user for user in users if user["email"] != user_to_delete]

        with open("usuarios.json", "w") as file:
            json.dump(updated_users, file, indent=4)
            
    def change_certificado_menu(self):
        self.screen_controller.clear_screen()
        self.root.title("Cambiar estado de certificado a un curso")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        self.root.user = ctk.CTkLabel(self.root, text="Ingrese el email del usuario a manejar: ")
        self.root.user.pack()

        self.root.user_entry = ctk.CTkEntry(self.root)
        self.root.user_entry.pack()

        self.root.course = ctk.CTkLabel(self.root, text="Ingrese el nombre del curso a manejar: ")
        self.root.course.pack()

        self.root.course_entry = ctk.CTkEntry(self.root)
        self.root.course_entry.pack()

        self.root.estado_curso_var = ctk.BooleanVar()
        self.root.estado_curso = ctk.CTkCheckBox(self.root, text="Estado de curso", variable=self.root.estado_curso_var, onvalue=True, offvalue=False)
        self.root.estado_curso.pack()

        self.root.delete_course_button = ctk.CTkButton(self.root, text="Cambiar estado de certificado", command=lambda: self.change_certificado(self.root.course_entry.get(), self.root.user_entry.get(), self.root.estado_curso_var.get()))
        self.root.delete_course_button.pack()
        
    def change_certificado(self, course, user, estado_curso):
        self.base_de_datos = BaseDeDatosJSON("usuarios.json")
        self.current_user = self.base_de_datos.buscar_usuario(user)
        
        if estado_curso:
            self.current_user["Cursos proximos"][course]["certificado"] = True
        else:
            self.current_user["Cursos proximos"][course]["certificado"] = False
        
        self.base_de_datos.save_data()
        

def main():
    root = ctk.CTk()
    admin = Administrador(root)
    admin.admin_login_menu()
    root.mainloop()

if __name__ == '__main__':
    main()