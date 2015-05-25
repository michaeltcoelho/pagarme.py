# coding:utf-8
from pagarme.api import default_api
from pagarme.resource import Resource
from pagarme.util import make_url


class Card(Resource):
    """Card class wrapping the REST /cards endpoint
    """