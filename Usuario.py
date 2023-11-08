'''
Universidad del Valle de Guatemala
Proyecto Final POO
Roberto Barreda - 23354
'''


class Usuario:
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
        return {
            "perfil": self.perfil,
            "Cursos realizados": self.cursos_realizados,
            "Cursos proximos": self.cursos_proximos
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["perfil"]["carnet"],
            data["perfil"]["name"],
            data["perfil"]["email"],
            data["perfil"]["password"],
            data["perfil"]["miembro_de_Salud"],
            data.get("Cursos realizados", []),
            data.get("Cursos proximos", [])
        )
