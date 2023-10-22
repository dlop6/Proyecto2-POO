import re
import json
from Usuario import Usuario

class ControladorUsuario:
    def __init__(self, base_de_datos):
        self.base_de_datos = base_de_datos

    def crear_cuenta(self, nombre, email, password, es_miembro_salud, carnet_colegiado=None):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return "Correo electrónico no válido"
        if len(password) < 6:
            return "La contraseña debe tener al menos 6 caracteres"
        if email in self.base_de_datos.data:
            return "El correo electrónico ya está registrado"

        usuario = Usuario(nombre, email, password, es_miembro_salud, carnet_colegiado)
        self.base_de_datos.agregar_usuario(email, usuario.to_dict())  # Serialize the user data
        return "Cuenta creada con éxito"

    def autenticar(self, email, password):
        usuario_data = self.base_de_datos.buscar_usuario(email)
        if usuario_data is None:
            return "Usuario no encontrado"

        usuario = Usuario.from_dict(usuario_data)  # Deserialize the user data
        if usuario.password != password:
            return "Contraseña incorrecta"
        return "Inicio de sesión exitoso"
