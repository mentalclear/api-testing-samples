import requests
import json

def get_hash_stats(stats_url):
    response = requests.get(stats_url)
    return json.loads(response.text)