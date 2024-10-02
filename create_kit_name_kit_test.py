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