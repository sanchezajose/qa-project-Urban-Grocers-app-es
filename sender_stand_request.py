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
