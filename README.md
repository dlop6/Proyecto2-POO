# README

## Descripción del Proyecto

Este proyecto ofrece un sistema integrado que combina la gestión de noticias relacionadas con medicina y salud y un sistema de cursos en línea con representación de usuarios. A continuación, se describen las principales clases y sus funcionalidades.

## Dependencias

Asegúrese de tener instaladas las siguientes dependencias antes de ejecutar el proyecto:

- `requests`: Para realizar solicitudes HTTP y obtener noticias de la API.
  ```bash
  pip install requests
  ```
- `customtkinter`: Una versión personalizada de Tkinter utilizada para la interfaz gráfica.
  ```bash
  pip install customtkinter
  ```

## Clase `Administrador`

La clase `Administrador` forma parte de un sistema que permite la gestión de usuarios y cursos. Proporciona funciones como iniciar sesión como administrador, eliminar usuarios y cambiar el estado de certificado de un curso para un usuario específico.

### Métodos Principales:

- `admin_login_menu`: Muestra el menú de inicio de sesión del administrador.
- `admin_menu`: Muestra el menú principal del administrador después de iniciar sesión.
- `delete_user_menu`: Muestra el menú para eliminar un usuario.
- `delete_user`: Elimina un usuario del sistema.
- `change_certificado_menu`: Muestra el menú para cambiar el estado del certificado de un curso para un usuario.
- `change_certificado`: Cambia el estado del certificado de un curso para un usuario.

## Clase `BaseDeDatosJSON`

La clase `BaseDeDatosJSON` representa una base de datos en formato JSON para almacenar información de usuarios y sus cursos. Proporciona funciones para cargar, guardar, buscar y actualizar información en la base de datos.

### Métodos Principales:

- `load_data`: Carga la información del archivo en el atributo data.
- `save_data`: Guarda la información del atributo data en el archivo.
- `buscar_usuario`: Busca un usuario por su email en el atributo data.
- `agregar_usuario`: Agrega un usuario con su información al atributo data.
- `autenticar`: Autentica a un usuario por su email y password.
- `crear_cuenta`: Crea una cuenta de usuario con su información y cursos realizados y próximos.

## Clase `Cursos`

La clase `Cursos` se encarga de gestionar los cursos de un usuario. Permite agregar nuevos cursos y eliminar cursos existentes.

### Métodos Principales:

- `agregar_curso`: Agrega un curso a la lista de cursos de un usuario.
- `eliminar_curso`: Elimina un curso de la lista de cursos de un usuario.

## Clase `News`

La clase `News` permite obtener y mostrar noticias relacionadas con medicina y salud en inglés desde la API de newsdata.io. Proporciona funciones para obtener noticias y mostrarlas en una interfaz gráfica de usuario.

### Métodos Principales:

- `get_news`: Obtiene las noticias de la API de newsdata.io.
- `news_menu`: Muestra las noticias obtenidas de la API en una interfaz gráfica de usuario.
- `view_article`: Muestra la descripción de una noticia en una ventana emergente.
- `open_link`: Abre el enlace de una noticia en el navegador web predeterminado.

## Ejecución del Proyecto

Para ejecutar el proyecto, se proporciona un script principal llamado `main` que crea instancias de las clases pertinentes y muestra menús o realiza otras acciones según sea el caso.

```bash
python main.py
```

Esperamos que este proyecto sea de utilidad y se adapte a sus necesidades. ¡Gracias por utilizar este sistema de noticias y gestión de cursos en línea!
