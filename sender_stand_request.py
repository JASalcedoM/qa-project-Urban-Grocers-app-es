import data
import configuration
import requests


#Función para crear un nuevo usuario.
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

#Función para crear un kit.
def create_new_kit(model):
    headers = data.headers.copy()
    token = create_new_user()
    headers["Authorization"] = f"Bearer {token}"

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=model,
                         headers=headers)

# Función para cambiar el valor del parámetro firstName en el cuerpo de la solicitud
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

#Función para crear un nuevo usuario.
def create_new_user():
    user_body = get_user_body("Pepe")
    user_response = post_new_user(user_body)
    token = user_response.json()["authToken"]
    return token

create_new_user()