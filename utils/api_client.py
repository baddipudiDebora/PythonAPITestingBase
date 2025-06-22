import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

    def get(self, endpoint, params=None, headers=None):
        return requests.get(f"{self.base_url}/{endpoint.lstrip('/')}", params=params, headers=headers)

    def post(self, endpoint, data=None, headers=None):
        return requests.post(f"{self.base_url}/{endpoint.lstrip('/')}", json=data, headers=headers)

    def put(self, endpoint, data=None, headers=None):
        return requests.put(f"{self.base_url}/{endpoint.lstrip('/')}", json=data, headers=headers)

    def delete(self, endpoint, headers=None):
        return requests.delete(f"{self.base_url}/{endpoint.lstrip('/')}", headers=headers)