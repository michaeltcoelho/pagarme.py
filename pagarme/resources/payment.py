# coding:utf-8
from pagarme.api import default_api
from pagarme.common import make_url

from .resource import Resource


class Payment(Resource):
    """`Payment`:class: wrapping the REST /payables endpoint
    """
    @classmethod
    def find(cls, payable_id):
        api = default_api()
        url = make_url('/payables', str(payable_id))
        return cls(api.get(url))

    @classmethod
    def all(cls, count=10, page=1):
        api = default_api()
        params = {'count': count, 'page': page}
        response = api.get('/payables', params=params)
        return [cls(item) for item in response]
