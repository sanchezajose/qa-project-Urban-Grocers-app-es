# Proyecto Urban Grocers 
## Proyecto para el séptimo sprint: Tarea
Otro QA Engineer que trabaja contigo está comprobando cómo la aplicación Urban Grocers crea kits de productos. Se han creado varias listas de comprobación,
una de ellas es para el campo name en la solicitud de creación de un kit de productos.

Tu tarea es automatizar las pruebas desde esta lista de comprobación, cargar el código en GitHub y enviar el repositorio a revisión.







## Acerca el proyecto:
Creación de un kit para el usuario o usuaria
Vas a crear un kit dentro de un usuario o usuaria particular, no una tarjeta. Para ello, sigue estos pasos:

Envía una solicitud para crear un nuevo usuario o usuaria y recuerda el token de autenticación (authToken).
Envía una solicitud para crear un kit personal para este usuario o usuaria. Asegúrate de pasar también el encabezado Autorization.
Después de eso, simplemente utiliza la lista de comprobación. Los resultados de la prueba serán diferentes cada vez, según el cuerpo de solicitud. Sin embargo, los pasos serán los mismos.

### Tecnologías a usar en este proyecto
- Lenguaje de Programamcion "Python 3.12"
- Consola Pycharm Community Edition 2024.2.1

## Configuración
> Trabajarás con Git y GitHub en este proyecto. Sigue los pasos a continuación para configurar tu proyecto.

>  Paso 1: conecta tu GitHub
El primer paso es enlazar tu cuenta de GitHub a TripleTen. Para ello, haz clic en el botón "Enlazar la cuenta de GitHub" en el widget en la parte superior de esta página. Esto te llevará a una nueva pestaña del navegador donde se te pedirá que confirmes que deseas enlazar tu cuenta de GitHub. Si aún no has iniciado sesión en GitHub, se te pedirá que introduzcas tu nombre de usuario y contraseña. Al confirmarlo, tu perfil de TripleTen se conectará a tu perfil de GitHub a través de la API segura de GitHub. Esto te permitirá enviar tus proyectos automáticamente con tan solo hacer clic en un botón, directamente dentro de la plataforma de TripleTen.

> Paso 2. Clona el repositorio en tu computadora
Una vez que hayas vinculado tu cuenta de TripleTen con GitHub, se creará un repositorio automáticamente. El nombre del repositorio será qa-project-Urban-Grocers-app-es.

> Ve a GitHub y clona el nuevo repositorio en tu computadora local, siguiendo estos pasos:

> Abre la línea de comandos en tu computadora (Git Bash).
> Si aún no lo has hecho, crea un directorio para almacenar todos tus proyectos. Por ejemplo:
```sh
cd ~               # asegúrate de estar en tu directorio de inicio
mkdir projects     # crea una carpeta llamada projects
cd projects        # cambia el directorio a la nueva carpeta de proyectos
```

> Clona el repositorio con SSH.
```sh
git clone git@github.com:sanchezajose/qa-project-Urban-Grocers-app-es.git
```
> Paso 3. Trabaja con el proyecto de forma local
Ahora tienes una copia local del proyecto y puedes abrir la carpeta del proyecto en tu computadora.
```sh
💡 Puedes utilizar PyCharm para trabajar en el proyecto localmente. Simplemente abre PyCharm y selecciona Archivo → Abrir y luego selecciona la carpeta qa-project-Urban-Grocers-app-es que clonaste en tu computadora.
```

#### Cuando puedas comenzar a trabajar, presiona el botón "Iniciar el servidor" para obtener la URL de tu servidor.
```sh
Servidor
¡Genial, tu servidor ha sido iniciado!

Dirección del banco: https://cnt-a85485b0-70a1-409f-b9eb-7809b8ae20de.containerhub.tripleten-services.com

 Documentación de la API: [https://cnt-a85485b0-70a1-409f-b9eb-7809b8ae20de.containerhub.tripleten-services.com/docs/]
```
Reiniciar el servido(BOTON)

Abre la documentación para estudiar la API de la aplicación de Urban Grocers: <the url of the launched server>/docs/.

## Dentro de Pycharm Community Edittion 2024 2.1
### Pasos previos :
- Instalar la libreria "Request":
    - A través de la interfaz de PyCharm en "Python Packages":
    - En tu proyecto de PyCharm, dirígete al panel inferior y selecciona la pestaña "Python Packages".
    - En el campo de búsqueda, introduce "Request".
    - Localiza y selecciona el paquete "Request" de la lista y haz clic en el botón "Install".
    

- Instalar la libreria "Pytest":
    - A través de la interfaz de PyCharm en "Python Packages":
    - En tu proyecto de PyCharm, dirígete al panel inferior y selecciona la pestaña "Python Packages".
    - En el campo de búsqueda, introduce "Pytest".
    - Localiza y selecciona el paquete "Pytest" de la lista y haz clic en el botón "Install".

> Pruebas para el parámetro "Name" al crear un kit dentro de un Usuari@ []
 Necesitas tener instalados los paquetes pytest y request para ejecutar las pruebas.
 Ejecuta todas las pruebas con el comando pytest.

### Lista de Comprobacion
 |№  |	Description	  |ER:  | Estado |
| ------ | ------ | ------ | ------ |
1|	El número permitido de caracteres (1): kit_body = { "name": "a"}|	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud| Aprobado
2|	El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}|	Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud| Aprobado
3|	El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }|	Código de respuesta: 400| No Aprobado
4|	El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }|	Código de respuesta: 400| No Aprobado
5|	Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }|	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud| Aprobado
6|	Se permiten espacios: kit_body = { "name": " A Aaa " }|	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud| Aprobado
7|	Se permiten números: kit_body = { "name": "123" }|	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud| Aprobado
8|	El parámetro no se pasa en la solicitud: kit_body = { }|	Código de respuesta: 400| No Aprobado
9|	Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }|	Código de respuesta: 400| No Aprobado

### Ejecución de pruebas
Tienes dos opciones para ejecutar tus pruebas: directamente desde la consola de PyCharm o utilizando su interfaz gráfica.

1️⃣ Desde la terminal de PyCharm

Dirígete a la pestaña "Terminal" en la parte inferior de PyCharm. Por defecto, esta terminal se ubica en el directorio de tu proyecto. 

Para ejecutar todas las pruebas de tu proyecto, simplemente escribe:
```sh
pytest
```
Luego ejecuta las pruebas desde el archivo create_kit_name_kit_test.py:
```sh
pytest create_kit_name_kit_test.py
```
### Ejecuta todas las pruebas del proyecto:

- En el menú "Run", selecciona "Edit Configurations" (Editar configuraciones).
- Haz clic en "+ (Add New Configuration)" (Agregar nueva configuración). Se abrirá una ventana nueva.
- Selecciona "Python tests → pytest" (Pruebas de Python → Pytest) en la lista de configuraciones.
Aparecerá una ventana nueva. 
- Selecciona "Custom" (Personalizar) en la línea "Target" (Objetivo).
- Haz clic en "Apply" (Aplicar) y luego en "OK" (Aceptar).
- Ahora haz clic en el ícono de la flecha verde para iniciar la configuración y observa los resultados.

### Ejecuta el Commit y el push desde Pycharm:

- En la barra "Archivos de arbol del proyecto", selecciona el boton "Commit", se despliega una ventana con una barra de seleccion con todos los archivos del proyecto.
- Haz clic en la casilla para seleccionar todos los archivos.
- Agrega un comentario "Entrega proyecto 7".
- Haz clic en el boton inferor izquierdo "Commit and Push"
- Se abrira una panttalla emergente y haz clic en el boton "Push".
- Ahora los archivos se han actualizado en el GitHuB ahora el equipo puedo ver este proyecto.


### Archivos dentro del proyecto (qa-project-Urban-Grocers-app-es)
- Configuration.py 
- Data.py
- Senser_stant_request.py
- Create_kit_name_kit_test.py
- .gitignore
- ReadMe.md

### Contenido del Archivo "Configuration.py"
Contiene todas las rutas Url necesarios para hacer los llamados de las Apis
```sh
URL_SERVICE = "https://cnt-3bc58b6c-2959-406f-b3a5-202a2a41fd79.containerhub.tripleten-services.com"
CREATE_USER_PATH = "/api/v1/users/"
KITS_PATH = "/api/v1/kits"
KITS_SAVE_PATH = "/api/v1/kits/search?name=Mi%20Conjunto"
```
### Contenido del Archivo "Data.py"
Contiene los bodys para desarrollar el proyecto
```sh
headers = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}
kit_body = {
       "name": "Mi Conjunto"
}
kit_one_letter = {
       "name": "A"
}
kit_511_letter = {
       "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
}
kit_0_letter = {
       "name": ""
}
kit_512_letter = {
       "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
}
kit_special_letter = {
       "name": "№%@"
}
kit_speace_letter = {
       "name": "A Aaa "
}
kit_str_number = {
       "name": "123"
}
kit_no_data = {
       
}
kit_int_number = {
       "name": 123
}
```
### Contenido del Archivo "Sender_stand_request.py"
Contiene las solicitudes HTTp(Get,Post) para desarrollar el proyecto
```sh
import configuration
import requests
import data
from data import user_body, kit_body

def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)


authToken = post_new_user(user_body).json()['authToken']
response = post_new_user(data.user_body)

def post_new_client_kit(kit_body):
    headers_kit = data.headers.copy()
    authorization = post_new_user(user_body).json()['authToken']
    headers_kit["Authorization"] = f'Bearer {authorization}'

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers_kit)


def get_new_client_kit(kit_body):
    headers_kit = data.headers.copy()
    authorization = post_new_user(user_body).json()['authToken']
    headers_kit["Authorization"] = f'Bearer {authorization}'

    return requests.get(configuration.URL_SERVICE + configuration.KITS_SAVE_PATH,
                        json=kit_body,
                        headers=headers_kit)

response = get_new_client_kit(kit_body)

```

### Contenido del Archivo "Create_kit_name_kit_test.py"
Contiene las funciones de prueba para hacer el test
```sh
import sender_stand_request
import data


def positive_assert(kit_body):
    response_kit_body = sender_stand_request.post_new_client_kit(kit_body)
    assert response_kit_body.status_code == 201
    assert response_kit_body.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    response_kit_body = sender_stand_request.post_new_client_kit(kit_body)
    assert response_kit_body.status_code == 400

    # Prueba 1. El número permitido de caracteres (1)
def test_create_kit_1_letter_in_kit_name_get_success_response():
    positive_assert(data.kit_one_letter)

# Prueba 2. El número permitido de caracteres (511)
def test_create_kit_511_letter_in_kit_name_get_success_response():
    positive_assert(data.kit_511_letter)

# Prueba 3. Error. 	El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_0_letter_in_kit_name_get_error_response():
    negative_assert_code_400(data.kit_0_letter)

def test_create_kit_512_letter_in_kit_name_get_error_response():
    negative_assert_code_400(data.kit_512_letter)

# Prueba 5. Se permiten caracteres especiales
def test_create_has_special_simbol_letter_in_kit_name_get_success_response():
    positive_assert(data.kit_special_letter)

# Prueba 6. Se permiten espacios
def test_create_has_space_between_letter_in_kit_name_get_success_response():
    positive_assert(data.kit_speace_letter)

# Prueba 7. Se permiten números tipo str
def test_create_user_has_number_in_kit_name_get_success_response():
    positive_assert(data.kit_str_number)


# Prueba 8. Error. Falta el parámetro Name en la solicitud
def test_create_user_no_kit_name_get_error_response():
    negative_assert_code_400(data.kit_no_data)

# Prueba 10. Error. El tipo del parámetro Name: número
def test_create_kit_number_type_kit_name_get_error_response():
    negative_assert_code_400(data.kit_int_number)
```
### Contenido del Archivo ".GitIgnore"
ontiene todas los archivos no necesarios o a ignorar dentro del proyecto
```sh
.pytest/
venv/
.idea/
.pytest_cache/
__pycache__/
```
### Contenido del Archivo "ReadMe.md"
Finalmente este archivo donde encontraras la informacion detallada de este proyecto
```sh
REadMe.mD
```
José Sánchez, 14Avo grupo,sprint 7
PROYECTO SPRINT 7

**Espero con gusto tu Feedback Te leo**










