'''
Universidad del Valle de Guatemala
Proyecto Final POO
Javier Lopez - 23415 y Roberto Barreda - 23354
'''
import tkinter as tk
import customtkinter as ctk
import uuid
class Cursos:
    def __init__(self) -> None:
        self.cursos = []
        self.cursos_disponibles = []

    def cursos_menu(self, usuario):
        root = tk.Tk()
        root.title("Cursos Disponibles")

        def agregar_curso(curso, fecha, cupo):
            if not usuario.curso_evaluado(curso["nombre"]):
                usuario.agregar_curso({"id": str(uuid.uuid4()), "nombre": curso["nombre"], "fecha": fecha, "cupo": cupo})
                self.cursos_disponibles.remove(curso)
                print(f"Curso {curso['nombre']} agregado a {usuario.perfil['name']}")
            else:
                print(f"El curso {curso['nombre']} ya ha sido evaluado por {usuario.perfil['name']}")

        def eliminar_curso(curso):
            self.cursos = [c for c in self.cursos if c['nombre'] != curso['nombre']]
            self.cursos_disponibles.append(curso)
            print(f"Curso {curso['nombre']} eliminado")

        def mostrar_cursos():
            for curso in self.cursos:
                print(f"Nombre: {curso['nombre']}, Fecha: {curso['fecha']}, Cupo: {curso['cupo']}")

        def mostrar_cursos_disponibles():
            for curso in self.cursos_disponibles:
                print(curso)

        label = tk.Label(root, text="Cursos Disponibles")
        label.pack(pady=10)

        cursos_frame = tk.Frame(root)
        cursos_frame.pack(pady=10)

        for curso in self.cursos_disponibles:
            tk.Label(cursos_frame, text=curso["nombre"]).pack(side=tk.TOP, pady=5)

            agregar_button = tk.Button(cursos_frame, text="Tomar Curso", command=lambda c=curso: agregar_curso(c, "Fecha Dummy", "Cupo Dummy"))
            agregar_button.pack(side=tk.TOP, pady=5)

        root.mainloop()
