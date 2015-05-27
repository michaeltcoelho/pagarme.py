# coding:utf-8
import base64
import rsa
from urllib import urlencode

from pagarme.api import default_api
from pagarme.resource import Resource
from pagarme.util import make_url


class CardHash(object):
    """`CardHash`:class: is a common to generate card hash key
    """
    @staticmethod
    def generate_hash_key(card):
        api = default_api()
        url = make_url('/transactions', '/card_hash_key')
        response = api.get(url, params={'encryption_key': api.encryption_key})
        response = Resource(response)
        if response.success():
            public_key = rsa.PublicKey.load_pkcs1_openssl_pem(response.public_key)
            response.card_hash = '%s_%s' % (response.id, base64.b64encode(rsa.encrypt(urlencode(card), public_key)))
        return response