# coding:utf-8
from pagarme.api import default_api
from pagarme.resource import Resource
from pagarme.util import make_url, merge_dict
from pagarme.metadata import MetaData, CustomerMetaData
from pagarme.exceptions import MetaDataInstanceError, CustomerInstanceError


class Transaction(Resource):
    """Transaction class wrapping the REST /transactions endpoint
    """
    def create(self, metadata=None, customer=None):

        if metadata and not isinstance(metadata, MetaData):
            raise MetaDataInstanceError('The metadata parameter must be an object of `MetaData`:class:')

        if customer and not isinstance(customer, CustomerMetaData):
            raise MetaDataInstanceError('The customer parameter must be an object of `CustomerMetaData`:class:')

        metadata = metadata.to_dict() if metadata else {}
        customer = customer.to_dict() if customer else {}
        response = self.api.post('/transactions', params=merge_dict(self.to_dict(), metadata, customer))
        self.assign(response)
        return self.success()

    def get_split_rules(self, split_rules_id, transaction_id=None):
        if not transaction_id:
            transaction_id = self.id
        url = make_url('/transactions', str(transaction_id), '/split_rules', str(split_rules_id))
        response = self.api.get(url)
        return Resource(response)

    def get_all_split_rules(self, transaction_id=None):
        if not transaction_id:
            transaction_id = self.id
        url = make_url('/transactions', str(transaction_id), '/split_rules')
        response = self.api.get(url)
        split_rules = [Resource(item) for item in response]
        return split_rules

    def get_payables(self, payable_id, transaction_id=None):
        if not transaction_id:
            transaction_id = self.id
        url = make_url('/transactions', str(transaction_id), '/payables', str(payable_id))
        response = self.api.get(url)
        return Resource(response)

    def get_all_payables(self, transaction_id=None):
        if not transaction_id:
            transaction_id = self.id
        url = make_url('/transactions', str(transaction_id), '/payables')
        response = self.api.get(url)
        payables = [Resource(item) for item in response]
        return payables

    def get_antifraud_analysis(self, analysis_id, transaction_id=None):
        if not transaction_id:
            transaction_id = self.id
        url = make_url('/transactions', str(transaction_id), '/antifraud_analyses', str(analysis_id))
        response = self.api.get(url)
        return Resource(response)

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

    @staticmethod
    def generate_hash_key():
        api = default_api()
        url = make_url('/transactions', '/card_hash_key')
        response = api.get(url, params={'encryption_key': api.encryption_key})
        return Resource(response)

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