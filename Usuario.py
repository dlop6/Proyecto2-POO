

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

    def __init__(self, carnet, nombre, email, password, es_miembro_salud, cursos_realizados=None, cursos_proximos=None):
        self.perfil = {
            "carnet": carnet,
            "name": nombre,
            "email": email,
            "password": password,
            "miembro_de_Salud": es_miembro_salud
        }
        self.cursos_realizados = cursos_realizados or []
        self.cursos_proximos = cursos_proximos or []

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
            data.get("Cursos proximos", [])
        )
