import configuration
import requests
import data
from data import user_body, kit_body


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)


authToken = post_new_user(user_body).json()['authToken']
response = post_new_user(data.user_body)
print(response.status_code)
print("Nuevo Usuario Creado", response.json())

headers_kit = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer {authToken}'
}

def post_new_client_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers_kit)

print(post_new_client_kit(kit_body).status_code, post_new_client_kit(kit_body).json()["name"])

def get_new_client_kit(kit_body):
    return requests.get(configuration.URL_SERVICE + configuration.KITS_SAVE_PATH,
                        json=kit_body,
                        headers=headers_kit)

kit_name = get_new_client_kit(kit_body).json()['name']
response = get_new_client_kit(kit_body)
print(response.status_code)