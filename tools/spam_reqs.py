import requests
import json

endpoint = "http://localhost:8088/hash"
payload = {"password": "testpassword"}


def send_post_to_local(url, data):
    """Continuously sending POST requests to the provided
    endpoint using the provided payload"""
    while True:
        try:
            response = requests.post(url, json=data)
            content = json.loads(response.text)
            print(f"Request #{content} | Status code: {response.status_code}")
        except (requests.ConnectionError, json.JSONDecodeError):
            print("Connection was refused by the remote host")
            return False


send_post_to_local(endpoint, payload)
