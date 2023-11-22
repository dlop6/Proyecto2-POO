

class Usuario:
    """
    Clase que representa a un usuario del sistema de cursos en línea.

    Atributos:
    - carnet (str): El número de carnet del usuario.
    - nombre (str): El nombre completo del usuario.
    - email (str): El correo electrónico del usuario.
    - password (str): La contraseña del usuario.
    - es_miembro_salud (bool): Indica si el usuario es miembro del sector salud.
    - cursos_realizados (list): Lista de cursos que el usuario ha completado.
    - cursos_proximos (list): Lista de cursos que el usuario tiene pendientes por completar.
    """

    def __init__(self, carnet, nombre, email, password, es_miembro_salud, cursos_realizados=None, cursos_proximos=None, evaluaciones=None):
        self.perfil = {
            "carnet": carnet,
            "name": nombre,
            "email": email,
            "password": password,
            "miembro_de_Salud": es_miembro_salud
        }
        self.cursos_realizados = cursos_realizados or []
        self.cursos_proximos = cursos_proximos or []
        self.evaluaciones = evaluaciones or []

    def to_dict(self):
        """
        Retorna un diccionario con la información del usuario.
        """
        return {
            "perfil": self.perfil,
            "Cursos realizados": self.cursos_realizados,
            "Cursos proximos": self.cursos_proximos
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crea una instancia de Usuario a partir de un diccionario con su información.

        Args:
        - data (dict): Diccionario con la información del usuario.

        Returns:
        - Usuario: Instancia de Usuario con la información del diccionario.
        """
        return cls(
            data["perfil"]["carnet"],
            data["perfil"]["name"],
            data["perfil"]["email"],
            data["perfil"]["password"],
            data["perfil"]["miembro_de_Salud"],
            data.get("Cursos realizados", []),
            data.get("Cursos proximos", []),
            data.get("evaluaciones", [])
        )

    def agregar_evaluacion_curso(self, nombre_curso, rating, comentarios):
        """
        Agrega una evaluación de curso al perfil del usuario.

        Args:
        - nombre_curso (str): Nombre del curso a evaluar.
        - rating (float): Calificación dada al curso.
        - comentarios (str): Comentarios sobre el curso.
        """
        evaluacion = {"curso": nombre_curso, "rating": rating, "comentarios": comentarios}
        self.evaluaciones.append(evaluacion)

    def curso_evaluado(self, nombre_curso):
        """
        Verifica si el usuario ya ha evaluado el curso.

        Args:
        - nombre_curso (str): Nombre del curso a verificar.

        Returns:
        - bool: True si el curso ya ha sido evaluado, False de lo contrario.
        """
        for evaluacion in self.evaluaciones:
            if evaluacion["curso"] == nombre_curso:
                return True
        return False

    def agregar_curso(self, curso):
        """
        Agrega un curso a la lista de cursos realizados del usuario.

        Args:
        - curso (dict): Información del curso a agregar.

        Returns:
        - bool: True si se agregó correctamente, False si el curso ya estaba en la lista.
        """
        if not self.curso_evaluado(curso["nombre"]):
            self.cursos_realizados.append(curso)
            return True
        else:
            return False
    
    def agregar_curso_usuario(self, curso):
        """
        Agrega un curso a la lista de cursos realizados del usuario.

        Args:
        - curso (dict): Información del curso a agregar.

        Returns:
        - bool: True si se agregó correctamente, False si el curso ya estaba en la lista.
        """
        if not self.curso_ya_agregado(curso):
            self.cursos_realizados.append(curso)
            return True
        else:
            return False

    def curso_ya_agregado(self, curso):
        """
        Verifica si el usuario ya ha agregado el curso.

        Args:
        - curso (dict): Información del curso a verificar.

        Returns:
        - bool: True si el curso ya ha sido agregado, False de lo contrario.
        """
        for curso_realizado in self.cursos_realizados:
            if curso_realizado["nombre"] == curso["nombre"]:
                return True
        return False
