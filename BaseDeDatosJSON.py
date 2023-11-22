import json

class BaseDeDatosJSON:
    """
    Clase que representa una base de datos en formato JSON para almacenar información de usuarios y sus cursos.

    Atributos:
    - filename (str): El nombre del archivo donde se guardará la información.
    - data (dict): Un diccionario que contiene la información de los usuarios y sus cursos.

    Métodos:
    - __init__(self, filename): Constructor de la clase. Recibe el nombre del archivo donde se guardará la información.
    - load_data(self): Carga la información del archivo en el atributo data.
    - save_data(self): Guarda la información del atributo data en el archivo.
    - buscar_usuario(self, email): Busca un usuario por su email en el atributo data.
    - agregar_usuario(self, email, usuario_data): Agrega un usuario con su información al atributo data.
    - autenticar(self, email, password): Autentica a un usuario por su email y password.
    - crear_cuenta(self, email, password, nombre, carnet, miembro_de_Salud, cursos_realizados=None, cursos_proximos=None): Crea una cuenta de usuario con su información y cursos realizados y próximos.
    """
    def __init__(self, filename):
        """
        Constructor de la clase BaseDeDatosJSON.

        Parámetros:
        - filename (str): El nombre del archivo donde se guardará la información.
        """
        self.filename = filename
        self.data = {}
        self.load_data()

    def load_data(self):
        """
        Carga la información del archivo en el atributo data.
        """
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}

    def save_data(self):
        """
        Guarda la información del atributo data en el archivo.
        """
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def buscar_usuario(self, email):
        """
        Busca un usuario por su email en el atributo data.

        Parámetros:
        - email (str): El email del usuario a buscar.

        Retorna:
        - El diccionario que representa al usuario si se encuentra en el atributo data, None en caso contrario.
        """
        for usuario in self.data['usuarios']:
            if usuario['perfil']['email'] == email:
                return usuario
        return None

    def agregar_usuario(self, email, usuario_data):
        """
        Agrega un usuario con su información al atributo data.

        Parámetros:
        - email (str): El email del usuario a agregar.
        - usuario_data (dict): Un diccionario que contiene la información del usuario a agregar.
        """
        self.data[email] = usuario_data
        self.save_data()
        
    def autenticar(self, email, password):
        """
        Autentica a un usuario por su email y password.

        Parámetros:
        - email (str): El email del usuario a autenticar.
        - password (str): La contraseña del usuario a autenticar.

        Retorna:
        - True si el usuario es autenticado exitosamente, False en caso contrario.
        """
        usuario = self.buscar_usuario(email)
        if usuario:
            return usuario['perfil']['password'] == password
        return False
    
    def crear_cuenta(self, email, password, nombre, carnet, miembro_de_Salud, cursos_realizados=None, cursos_proximos=None):
        """
        Crea una cuenta de usuario con su información y cursos realizados y próximos.

        Parámetros:
        - email (str): El email del usuario a crear.
        - password (str): La contraseña del usuario a crear.
        - nombre (str): El nombre del usuario a crear.
        - carnet (str): El carnet del usuario a crear.
        - miembro_de_Salud (bool): Indica si el usuario es miembro de Salud o no.
        - cursos_realizados (list): Una lista de diccionarios que representan los cursos realizados por el usuario. Opcional, por defecto es una lista vacía.
        - cursos_proximos (list): Una lista de diccionarios que representan los cursos próximos del usuario. Opcional, por defecto es una lista vacía.

        Retorna:
        - True si el usuario es creado exitosamente, False en caso contrario.
        """
        if cursos_realizados is None:
            cursos_realizados = []
        if cursos_proximos is None:
            cursos_proximos = []
        
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
    
    def obtener_cursos_usuario(self, email):
        """
        Obtiene la lista de cursos de un usuario.

        Parámetros:
        - email (str): El email del usuario.

        Retorna:
        - Una lista de cursos del usuario, o None si el usuario no existe.
        """
        usuario = self.buscar_usuario(email)
        if usuario:
            return usuario.get("Cursos realizados", [])
        return None
    
    def obtener_evaluaciones_usuario(self, email):
        """
        Obtiene las evaluaciones de cursos de un usuario.

        Parámetros:
        - email (str): El email del usuario.

        Retorna:
        - Una lista de evaluaciones de cursos del usuario, o None si el usuario no existe.
        """
        usuario = self.buscar_usuario(email)
        if usuario:
            return usuario.get("Evaluaciones de cursos", [])
        return None