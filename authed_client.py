from hitbtc_client.client import Client

class AuthedClient(Client):
    def __init__(self, public_key, secret):
        super().__init__()
        self.auth(public_key, secret)
