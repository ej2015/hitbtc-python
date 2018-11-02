from hitbtc_client.custom_session import CustomSession

class Client:
    '''API 2.0'''

    def __init__(self):
        url = "https://api.hitbtc.com" + "/api/2/"
        self.session = CustomSession(base_url = url)

    def auth(self, public_key, secret):
        self.session.auth = (public_key, secret)

    def get_address(self, currency_code):
        """Get address for deposit."""
        return self.session.get("account/crypto/address/%s" % (currency_code))

    def get_account_balance(self):
        """Get main balance."""
        return self.session.get("account/balance")

    def get_trading_balance(self):
        """Get trading balance."""
        return self.session.get("trading/balance")

    def transfer(self, currency_code, amount, to_exchange):
        return self.session.post("account/transfer", data={
            'currency': currency_code, 'amount': amount,
            'type': 'bankToExchange' if to_exchange else 'exchangeToBank'
            })

    def new_order(self, client_order_id, symbol_code, side, quantity, price=None):
        """Place an order."""
        data = {'symbol': symbol_code, 'side': side, 'quantity': quantity}

        if price is not None:
            data['price'] = price

        return self.session.put("order/%s" % (client_order_id), data=data)

    def get_order(self, client_order_id, wait=None):
        """Get order info."""
        data = {'wait': wait} if wait is not None else {}

        return self.session.get("order/%s" % (client_order_id), params=data)

    def cancel_order(self, client_order_id):
        """Cancel order."""
        return self.session.delete("order/%s" % (client_order_id))

    def withdraw(self, currency_code, amount, address, network_fee=None):
        """Withdraw."""
        data = {'currency': currency_code, 'amount': amount, 'address': address}

        if network_fee is not None:
            data['networkfee'] = network_fee

        return self.session.post("account/crypto/withdraw", data=data)

    def get_transaction(self, transaction_id):
        """Get transaction info."""
        return self.session.get("account/transactions/%s" % (transaction_id))

    def symbols(self):
        '''Available currency symbols'''
        return self.session.get("public/symbol")

    def symbol(self, symbol):
        '''Get symbol info'''
        return self.session.get(f"public/symbol/{symbol}")

    def currencies(self):
        '''Available currencies'''
        return self.session.get("public/currency")

    def currency(self, currency):
        '''Get currency info'''
        return self.session.get(f"public/currency/{currency}")

    def tickers(self):
        '''Ticker list for all symbols'''
        return self.session.get("public/ticker")

    def ticker(self, symbol):
        '''Ticker for symbol'''
        return self.session.get(f"public/ticker/{symbol}")

    def trades(self, symbol, params = None):
        '''trades for symbol'''
        return self.session.get(f"public/trades/{symbol}", params = params)

    def orderbook(self, symbol, params = None):
        '''orderbook for symbol'''
        return self.session.get(f"public/orderbook/{symbol}", params = params)

    def candles(self, symbol, params = None):
        '''candles for symbol'''
        return self.session.get(f"public/candles/{symbol}", params = params)

