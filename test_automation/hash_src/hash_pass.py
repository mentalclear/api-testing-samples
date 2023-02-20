import requests
import json


def hash_the_provided_password(url, payload):
    """ 
    This function sends a POST request to the provided URL using provided payload. 
    Expected paload: {"password": "{password of interest}"}
    Returns a tuple with a response dictionary and the status code
    """
    response = requests.post(url, json=payload)
    content = json.loads(response.text)
    return (content, response.status_code)