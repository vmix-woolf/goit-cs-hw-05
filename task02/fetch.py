import requests


def fetch_text(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text
