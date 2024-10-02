import sender_stand_request
import data
from data import kit_body



# Función para cambiar el valor del parámetro Name en el cuerpo de la solicitud
def get_new_client_kit(kit_name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = kit_name
    return current_kit_body

# Función de prueba positiva
def positive_assert(kit_name):
    kit_body = get_new_client_kit(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] != ""


# Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres
def negative_assert(kit_name):
    kit_body = get_new_client_kit(kit_name)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400



 #FUNCION POSITIVA
def positive_assert_has_kit_name(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 201
    assert response.json()["name"] != ""


# Función de prueba negativa cuando el error es "No se enviaron todos los parámetros requeridos"
def negative_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400

def positive_assert_symbol(kit_name):
        kit_body = get_new_client_kit(kit_name)
        response = sender_stand_request.post_new_client_kit(kit_body)
        assert response.status_code == 201
        assert response.json()["name"] == kit_name

    # Prueba 1. El número permitido de caracteres (1)
def test_create_kit_2_letter_in_kit_name_get_success_response():
    positive_assert("A")

# Prueba 2. El número permitido de caracteres (511)
def test_create_kit_511_letter_in_kit_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Prueba 3. Error. 	El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_0_letter_in_kit_name_get_success_response():
    negative_assert("")

def test_create_kit_512_letter_in_kit_name_get_success_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Prueba 5. Se permiten caracteres especiales
def test_create_has_special_simbol_letter_in_kit_name_get_success_response():
    positive_assert_symbol("№%@")

# Prueba 6. Se permiten espacios
def test_create_has_space_between_letter_in_kit_name_get_success_response():
    positive_assert("A Aaa ")

# Prueba 7. Se permiten números tipo str
def test_create_user_has_number_in_kit_name_get_success_response():
    positive_assert_symbol("123")

# Prueba 8. Error. Falta el parámetro Name en la solicitud
def test_create_user_no_kit_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400

# Prueba 10. Error. El tipo del parámetro Name: número
def test_create_kit_number_type_kit_name_get_error_response():
    kit_body = get_new_client_kit(12)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400