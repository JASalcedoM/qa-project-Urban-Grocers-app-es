import data
import sender_stand_request


# Función para cambiar el valor del parámetro firstName en el cuerpo de la solicitud
def get_user_body(first_name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body = data.user_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["firstName"] = first_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body

#Función para crear un nuevo usuario.
def create_new_user():
    user_body = get_user_body("Pepe")
    user_response = sender_stand_request.post_new_user(user_body)
    print(user_response.status_code)
    print(user_response.json())

create_new_user()