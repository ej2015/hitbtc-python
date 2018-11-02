from requests import Session
from urllib.parse import urljoin
from hitbtc_client import response

class CustomSession(Session):
    def __init__(self, base_url = None):
        super().__init__()
        self.base_url = base_url

    def request(self, method, url, *args, **kwargs):
        url = urljoin(self.base_url, url)
        res = super().request(method, url, *args, **kwargs)
        return response.CustomResponse(res).response()
