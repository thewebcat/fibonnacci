import requests


class Client:
    session = requests.Session()

    def __init__(self, endpoint_url):
        self.endpoint_url = endpoint_url

        self.session = requests.Session()

    def request(self, path, **kwargs):
        response = self.session.request(
            url='{}{}'.format(self.endpoint_url, path),
            **kwargs
        )
        response.raise_for_status()

        return response.json()