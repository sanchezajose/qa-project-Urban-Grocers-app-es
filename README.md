# Proyecto Urban Grocers 

## Acerca el proyecto:
Creación de un kit para el usuario o usuaria
Vas a crear un kit dentro de un usuario o usuaria particular, no una tarjeta. Para ello, sigue estos pasos:

Envía una solicitud para crear un nuevo usuario o usuaria y recuerda el token de autenticación (authToken).
Envía una solicitud para crear un kit personal para este usuario o usuaria. Asegúrate de pasar también el encabezado Autorization.
Después de eso, simplemente utiliza la lista de comprobación. Los resultados de la prueba serán diferentes cada vez, según el cuerpo de solicitud. Sin embargo, los pasos serán los mismos.

### Tecnologías a usar en este proyecto
- Lenguaje de Programamcion "Python 3.12"
- Consola Pycharm Community Edition 2024.2.1

## Pasos previos :
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










José Sánchez, 14Avo grupo,sprint 7
## PROYECTO SPRINT 7




 - Pruebas para el parámetro "Name" al crear un kit dentro de un Usuari@ []
- Necesitas tener instalados los paquetes pytest y request para ejecutar las pruebas.
- Ejecuta todas las pruebas con el comando pytest.

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
       "": ""
}
kit_int_number = {
       "name": 123
}
```
### Contenido del Archivo "Sender_stand_request.py"
Contiene todas los solicitudes Apis (Get,Post), requeridas para este ejercicio.
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
print(response.status_code)
print("Nuevo Usuario Creado", response.json())

def post_new_client_kit(kit_body):
    headers_kit = data.headers.copy()
    authorization = post_new_user(user_body).json()['authToken']
    headers_kit["Authorization"] = f'Bearer {authorization}'

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers_kit)

print(post_new_client_kit(kit_body).status_code, post_new_client_kit(kit_body).json()["name"])

def get_new_client_kit(kit_body):
    headers_kit = data.headers.copy()
    authorization = post_new_user(user_body).json()['authToken']
    headers_kit["Authorization"] = f'Bearer {authorization}'

    return requests.get(configuration.URL_SERVICE + configuration.KITS_SAVE_PATH,
                        json=kit_body,
                        headers=headers_kit)

kit_name = get_new_client_kit(kit_body).json()['name']
response = get_new_client_kit(kit_body)
print(response.status_code)
```
### Contenido del Archivo "Create_kit_name_kit_test.py"
Contiene todas las funciones necesarias para la Automatizacion de las pruebas del ejercicio a realizar.
```sh
import sender_stand_request
import data


# Función para cambiar el valor del parámetro Name en el cuerpo de la solicitud
def get_new_client_kit(kit_body):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = kit_body
    return current_kit_body

def positive_assert(kit_body):
    kit_body = get_new_client_kit(kit_body)
    response_kit_body = sender_stand_request.post_new_client_kit(kit_body)
    assert response_kit_body.status_code == 201
    assert response_kit_body.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    kit_body = get_new_client_kit(kit_body)
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
### Contenido del Archivo " .gitignore"
Contiene todas los archivos no necesarios o a ignorar dentro del proyecto
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
**Espero con gusto tu Feedback Te leo**










