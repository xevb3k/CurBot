from config import *
import json
import requests


class APIException(Exception):
    pass


class Convert:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException('Валюты должны быть разные')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не смог обработать валюту "{quote}"')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не смог обработать валюту "{base}"')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не смог обработать количество "{amount}"')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        res = float(json.loads(r.content)[keys[base]] * amount)
        return res
