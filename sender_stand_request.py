import data
import configuration
import requests


#Función para crear un nuevo usuario.
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers_user)

#función para crear un kit dando un auth token
def create_new_kit(model):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=model,
                         headers=data.headers)