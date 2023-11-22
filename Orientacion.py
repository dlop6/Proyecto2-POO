import customtkinter as ctk
from BaseDeDatosJSON import BaseDeDatosJSON

class Orientacion:
    def __init__(self, root, filename):
        self.root = root
        self.filename = filename
        self.base_de_datos = BaseDeDatosJSON(filename)
        self.usuarios = self.base_de_datos.data.get("usuarios", [])

    def mostrar_orientacion(self):
        self.root.geometry("500x600")
        self.root.title_label = ctk.CTkLabel(self.root, text="Orientación", font=("Arial", 16, "bold"))
        self.root.title_label.pack(pady=15, padx=10)

        for usuario in self.usuarios:
            self.mostrar_info_usuario(usuario)

    def mostrar_info_usuario(self, usuario):
        self.root.usuario_label = ctk.CTkLabel(self.root, text=f"Nombre: {usuario['perfil']['name']}, Email: {usuario['perfil']['email']}", font=("Arial", 12, "bold"))
        self.root.usuario_label.pack(pady=10, padx=10)

        evaluaciones = self.base_de_datos.obtener_evaluaciones_usuario(usuario['perfil']['email'])
        if evaluaciones:
            self.mostrar_evaluaciones_curso(evaluaciones)

    def mostrar_evaluaciones_curso(self, evaluaciones):
        self.root.eval_label = ctk.CTkLabel(self.root, text="Evaluaciones de Cursos", font=("Arial", 12, "bold"))
        self.root.eval_label.pack(pady=5, padx=10)

        for evaluacion in evaluaciones:
            self.root.eval_curso_label = ctk.CTkLabel(self.root, text=f"Curso: {evaluacion['nombre']}, Rating: {evaluacion['rating']}, Comentarios: {evaluacion['comentarios']}", wraplength=500)
            self.root.eval_curso_label.pack(pady=5, padx=10)

def main():
    root = ctk.CTk()
    orientacion = Orientacion(root, "usuarios.json")
    orientacion.mostrar_orientacion()
    root.mainloop()

if __name__ == "__main__":
    main()