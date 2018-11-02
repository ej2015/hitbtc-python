#HITBTC API PYTHON CLIENT#

HitBTC REST API 2.0 client

Initialize client:

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


