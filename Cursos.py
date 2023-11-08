'''
Universidad del Valle de Guatemala
Proyecto Final POO
Javier Lopez - 23415
'''

class Cursos:
    def __init__(self) -> None:
        self.cursos = []
        self.cursos_disponibles = []
        self.cursos_disponibles.append("Curso 1")
        self.cursos_disponibles.append("Curso 2")
        self.cursos_disponibles.append("Curso 3")
        self.cursos_disponibles.append("Curso 4")
        self.cursos_disponibles.append("Curso 5")

    def agregar_curso(self, curso, fecha, cupo):
        self.cursos.append({'curso': curso, 'fecha': fecha, 'cupo': cupo})
        self.cursos_disponibles.remove(curso)

    def eliminar_curso(self, curso):
        self.cursos.remove(curso)
        self.cursos_disponibles.append(curso)
    
    def mostrar_cursos(self):
        for curso in self.cursos:
            print(f"Nombre: {curso['nombre']}, Fecha: {curso['fecha']}, Cupo: {curso['cupo']}")