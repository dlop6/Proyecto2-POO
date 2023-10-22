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
        return self.data.get(email)

    def agregar_usuario(self, email, usuario_data):
        self.data[email] = usuario_data
        self.save_data()
