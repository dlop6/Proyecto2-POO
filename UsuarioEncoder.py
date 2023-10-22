import json

from Usuario import Usuario

class UsuarioEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Usuario):
            return {
                "nombre": obj.nombre,
                "email": obj.email,
                "password": obj.password,
                "es_miembro_salud": obj.es_miembro_salud,
                "carnet_colegiado": obj.carnet_colegiado
            }
        return super().default(obj)
