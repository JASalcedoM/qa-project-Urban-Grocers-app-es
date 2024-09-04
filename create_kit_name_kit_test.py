from venv import create

import data
import sender_stand_request
from data import kit_model


#función para cambiar el nombre del kit dentro del cuerpo de la solicitud
def get_kit_data(name):
    current_model = data.kit_model.copy()
    current_model["name"] = name
    return current_model

#función de prueba positiva para creación de kit
def positive_assert(name):
    kit_data = get_kit_data(name)
    kit_response = sender_stand_request.create_new_kit(kit_data)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name

#Función de prueba negativa para creación de kit
def negative_assert(name):
    kit_data = get_kit_data(name)
    kit_response = sender_stand_request.create_new_kit(kit_data)
    assert kit_response.status_code == 400

#Función de prueba negativa para creación de kit sin nombre
def negative_assert_no_name(kit_data):
    kit_response = sender_stand_request.create_new_kit(kit_data)
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400

#Función para crear un kit con una letra
def test_create_kit_1_letter_get_success_response():
    positive_assert(data.one_letter)

#Función para crear un kit con 511 letras
def test_create_kit_511_letter_get_success_response():
    positive_assert(data.upper_limit)

#Función para crear un kit sin caracteres
def test_create_kit_no_characters_get_error_response():
    negative_assert(data.no_characters)

#Función para crear un kit con 512 letras
def test_create_kit_512_letter_get_error_response():
    negative_assert(data.exceeded_limit)

#Función para crear un kit con carácteres especiales
def test_create_kit_special_characters_get_success_response():
    positive_assert(data.special_characters)

#Función para crear un kit con espacios
def test_create_kit_blank_spaces_allowed_get_success_response():
    positive_assert(data.string_with_blank_space)

#Función para crear un kit con números en string
def test_create_kit_numbers_allowed_get_success_response():
    positive_assert(data.numbers_string)

#Función para crear un kit sin el campo nombre
def test_create_kit_no_name_on_the_request_get_error_response():
    kit_data = data.kit_model.copy()
    kit_data.pop("name")
    negative_assert_no_name(kit_data)

#Función para crear un kit con data tipo número
def test_create_kit_different_data_type_not_allowed_get_error_response():
    negative_assert(data.numbers)