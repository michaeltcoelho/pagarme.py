# coding:utf-8
import base64
import rsa
from urllib import urlencode

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
            raise CustomerInstanceError('The customer parameter must be an object of `CustomerMetaData`:class:')

        customer = customer.to_dict() if customer else {}
        metadata = metadata.to_dict() if metadata else {}
        response = self.api.post('/transactions', params=merge_dict(self.to_dict(), customer, metadata))
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
    def generate_hash_key(card):
        api = default_api()
        url = make_url('/transactions', '/card_hash_key')
        response = api.get(url, params={'encryption_key': api.encryption_key})
        response = Resource(response)
        if response.success():
            public_key = rsa.PublicKey.load_pkcs1_openssl_pem(response.public_key)
            response.card_hash = '%s_%s' % (response.id, base64.b64encode(rsa.encrypt(urlencode(card), public_key)))
        return response

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