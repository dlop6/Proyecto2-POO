'''
Universidad del Valle de Guatemala
Proyecto Final POO
Roberto Barreda - 23354
'''


import json

class BaseDeDatosJSON:
    def __init__(self, filename):
        self.filename = filename
        self.data = {}
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def buscar_usuario(self, email):
        for usuario in self.data['usuarios']:
            if usuario['perfil']['email'] == email:
                return usuario
        return None

    def agregar_usuario(self, email, usuario_data):
        self.data[email] = usuario_data
        self.save_data()
        
    def autenticar(self, email, password):
        usuario = self.buscar_usuario(email)
        if usuario:
            return usuario['perfil']['password'] == password
        return False
    
    def crear_cuenta(self, email, password, nombre, carnet, miembro_de_Salud, cursos_realizados=None, cursos_proximos=None):
        if cursos_realizados is None:
            cursos_realizados = []
        if cursos_proximos is None:
            cursos_proximos = []
        
        # Check if email already exists
        if self.buscar_usuario(email):
            return False
        
        usuario = {
            "perfil": {
                "email": email,
                "password": password,
                "name": nombre,
                "carnet": carnet,
                "miembro_de_Salud": miembro_de_Salud
            },
            "Cursos realizados": cursos_realizados,
            "Cursos proximos": cursos_proximos
        }
        
        self.data['usuarios'].append(usuario)
        self.save_data()
        return True
