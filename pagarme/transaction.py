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

    def get_antifraud_analysis(self, analysis_id, transaction_id=None):

        if not transaction_id:
            transaction_id = self.id

        url = make_url('/transactions', str(transaction_id), '/antifraud_analyses', str(analysis_id))
        response = self.api.get(url)
        analysis = [Resource(item) for item in response]
        return analysis

    def get_all_antifraud_analysis(self, transaction_id=None):

        if not transaction_id:
            transaction_id = self.id

        url = make_url('/transactions', str(transaction_id), '/antifraud_analyses')
        response = self.api.get(url)
        analysis = [Resource(item) for item in response]
        return analysis

    def collect_payment(self, transaction_id=None):

        if not transaction_id:
            transaction_id = self.id

        url = make_url('/transactions', str(transaction_id), '/collect_payment')
        response = self.api.post(url)
        self.assign(response)
        return self.success()

    def capture(self, transaction_id):
        url = make_url('/transactions', str(transaction_id), '/capture')
        response = self.api.post(url)
        self.assign(response)
        return self.success()

    def refund(self, transaction_id):
        url = make_url('/transactions', str(transaction_id), '/refund')
        response = self.api.post(url)
        self.assign(response)
        return self.success()

    @classmethod
    def find(cls, transaction_id):
        api = default_api()
        url = make_url('/transactions', str(transaction_id))
        return cls(api.get(url))

    @classmethod
    def all(cls, count=10, page=1):
        api = default_api()
        params = {'count': count, 'page': page}
        responses = api.get('/transactions', params=params)
        return [cls(item) for item in responses]