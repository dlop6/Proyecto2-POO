'''
Universidad del Valle de Guatemala
Proyecto Final POO
Roberto Barreda - 23354
'''

import json

class Usuario:
    def __init__(self, nombre, email, password, es_miembro_salud, carnet_colegiado=None):
        self.nombre = nombre
        self.email = email
        self.password = password
        self.es_miembro_salud = es_miembro_salud
        self.carnet_colegiado = carnet_colegiado

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "email": self.email,
            "password": self.password,
            "es_miembro_salud": self.es_miembro_salud,
            "carnet_colegiado": self.carnet_colegiado
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["nombre"], data["email"], data["password"], data["es_miembro_salud"], data["carnet_colegiado"])
