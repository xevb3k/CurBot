from config import *
import json
import requests


class ConvertionException(Exception):
    pass


class Convert:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException('Валюты должны быть разные')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не смог обработать валюту "{quote}"')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не смог обработать валюту "{base}"')

        try:
            amount = int(amount)
        except ValueError:
            raise ConvertionException(f'Не смог обработать количество "{amount}"')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        res = float(json.loads(r.content)[keys[base]] * amount)
        return res
