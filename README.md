# HITBTC API PYTHON CLIENT

HitBTC REST API 2.0 client. Please refer to this [link](https://github.com/hitbtc-com/hitbtc-api). Some code are taken from the sample there.

## Initialize client

```
from hitbtc_client.client import Client

client = Client() 

#before you are able to call the private actions:
client.auth(public_key, secret)

```

You can use AuthedClient as a shortcut:

```
from hitbtc_client.authed_client import AuthedClient

client = AuthedClient(public_key, secret)
```


