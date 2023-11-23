import json
import tkinter as tk
from tkinter import messagebox

class Cursos:
    def __init__(self, user, root):
        self.email = user["perfil"]["email"]
        self.cursos_proximos = user["Cursos proximos"]  
        self.root = root

    def agregar_curso(self, curso):
    # Load the JSON data
        with open('usuarios.json', 'r') as f:
            data = json.load(f)

        # Find the user and check if the course already exists
        for usuario in data['usuarios']:
            if usuario['perfil']['email'] == self.email:
                for curso_existente in usuario['Cursos proximos']:
                    if curso_existente["codigo"] == curso["codigo"]:
                        self.show_message("Ya existe el curso!")
                        return

                # If the course does not exist, append it
                usuario['Cursos proximos'].append(curso)
                self.show_message("Curso agregado exitosamente!")
                break

        # Write the updated data back to the JSON file
        with open('usuarios.json', 'w') as f:
            json.dump(data, f, indent=4)
        

    def eliminar_curso(self, codigo):
    
        with open('usuarios.json', 'r') as f:
            data = json.load(f)

    
        for usuario in data['usuarios']:
            if usuario['perfil']['email'] == self.email:
                for curso in usuario['Cursos proximos']:
                    if curso["codigo"] == codigo:
                        usuario['Cursos proximos'].remove(curso)
                        self.show_message("Curso eliminado exitosamente!")
                        break
                else:
                    self.show_message("Curso no encontrado!")
                    return

    
        with open('usuarios.json', 'w') as f:
            json.dump(data, f, indent=4)

    def show_message(self, message):
        messagebox.showinfo("Message", message)
