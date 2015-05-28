# coding:utf-8
from pagarme.api import default_api
from pagarme.common import make_url

from .resource import Resource


class Recipient(Resource):
    """`Recipient`:class: wrapping the REST /recipients endpoint
    """
    def create(self):
        response = self.api.post('/recipients', data=self.to_dict())
        self.assign(response)
        return self.success()

    def balance(self, recipient_id=None):
        if not recipient_id:
            recipient_id = self.id
        url = make_url('/recipients', str(recipient_id), '/balance')
        response = self.api.get(url)
        return Resource(response)

    def balance_operations(self, recipient_id=None):
        if not recipient_id:
            recipient_id = self.id
        url = make_url('/recipients', str(recipient_id), '/balance', '/operations')
        response = self.api.get(url)
        operations = [Resource(item) for item in response]
        return operations

    def balance_operations_by_id(self, balance_operation_id, recipient_id=None):
        if not recipient_id:
            recipient_id = self.id
        url = make_url('/recipients', str(recipient_id), '/balance', '/operations', str(balance_operation_id))
        response = self.api.get(url)
        return Resource(response)

    @classmethod
    def find(cls, customer_id):
        api = default_api()
        url = make_url('/recipients', str(customer_id))
        return cls(api.get(url))

    @classmethod
    def all(cls, count=10, page=1):
        api = default_api()
        params = {'count': count, 'page': page}
        response = api.get('/recipients', params=params)
        return [cls(item) for item in response]
