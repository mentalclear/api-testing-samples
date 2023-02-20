import requests


def get_generated_hash_status_code(url_with_hash_id):
    response = requests.get(url_with_hash_id)
    return response.status_code


def get_generated_hash(url_with_hash_id):
    response = requests.get(url_with_hash_id)
    return response.text
