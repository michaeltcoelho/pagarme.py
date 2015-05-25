# coding:utf-8
from pagarme.api import default_api
from pagarme.resource import Resource
from pagarme.util import make_url


class Subscription(Resource):
    """Subscription class wrapping the REST /subscription endpoint
    """