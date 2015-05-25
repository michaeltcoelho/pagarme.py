# coding:utf-8
from pagarme.api import default_api
from pagarme.resource import Resource
from pagarme.util import make_url


class Transaction(Resource):
    """Transaction class wrapping the REST /transactions endpoint
    """
    def create(self):
        response = self.api.post('/transactions', self.to_dict())
        self.assign(response)
        return self.success()

    def refund(self, transaction_id):
        url = make_url('/transactions', str(transaction_id), '/refund')

    @classmethod
    def find(cls, transaction_id, bank):
        api = default_api()
        url = make_url('/transactions', str(transaction_id))
        return cls(api.get(url))

    @classmethod
    def all(cls, count=10, page=1):
        api = default_api()
        params = {'count': count, 'page': page}
        responses = api.get('/transactions', params=params)
        return [cls(item) for item in responses]