"""Source app with worthless data."""
import requests

def api_name(app):
    ''' example method '''
    endpoint = ''
    params = {
        "a1" : "1",
        "a2" : "2"
    }
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    req = requests.get(endpoint, params=params, headers=headers)
    result = req.json()
    return result