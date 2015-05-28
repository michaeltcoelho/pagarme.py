# coding:utf-8
from pagarme.api import default_api
from pagarme.common import make_url

from .resource import Resource


class BankAccount(Resource):
    """`BankAccount`:class: wrapping the REST /bank_accounts endpoint
    """
    def create(self):
        response = self.api.post('/bank_accounts', self.to_dict())
        self.assign(response)
        return self.success()

    @classmethod
    def find(cls, bank_account_id):
        api = default_api()
        url = make_url('/bank_accounts', str(bank_account_id))
        return cls(api.get(url))

    @classmethod
    def all(cls, count=10, page=1):
        api = default_api()
        params = {'count': count, 'page': page}
        responses = api.get('/bank_accounts', params=params)
        return [cls(item) for item in responses]
