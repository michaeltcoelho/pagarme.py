# coding:utf-8
from pagarme.api import default_api
from pagarme.common import make_url

from .resource import Resource


class Customer(Resource):
    """`Customer`:class: wrapping the REST /customers endpoint
    """
    def create(self):
        response = self.api.post('/customers', data=self.to_dict())
        self.assign(response)
        return self.success()

    @classmethod
    def find(cls, customer_id):
        api = default_api()
        url = make_url('/customers', str(customer_id))
        return cls(api.get(url))

    @classmethod
    def all(cls, count=10, page=1):
        api = default_api()
        params = {'count': count, 'page': page}
        response = api.get('/customers', params=params)
        return [cls(item) for item in response]
