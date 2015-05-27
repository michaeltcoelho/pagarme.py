# coding:utf-8
import base64
import rsa
from urllib import urlencode

from pagarme.api import default_api
from pagarme.resource import Resource
from pagarme.util import make_url


class Transaction(Resource):
    """Transaction class wrapping the REST /transactions endpoint
    """
    def create(self):
        response = self.api.post('/transactions', data=self.to_dict())
        self.assign(response)
        return self.success()

    def collect_payment(self, transaction_id=None):
        if not transaction_id:
            transaction_id = self.id
        url = make_url('/transactions', str(transaction_id), '/collect_payment')
        response = self.api.post(url)
        self.assign(response)
        return self.success()

    def capture(self, transaction_id=None):
        if not transaction_id:
            transaction_id = self.id
        url = make_url('/transactions', str(transaction_id), '/capture')
        response = self.api.post(url)
        self.assign(response)
        return self.success()

    def refund(self, transaction_id=None):
        if not transaction_id:
            transaction_id = self.id
        url = make_url('/transactions', str(transaction_id), '/refund')
        response = self.api.post(url)
        self.assign(response)
        return self.success()

    def calculate_installments_amount(self, installment):
        url = make_url('/transactions', '/calculate_installments_amount')
        response = self.api.get(url, params=installment)
        return Resource(response['installments'])

    def get_split_rules_by_id(self, split_rules_id, transaction_id=None):
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

    def get_payables_by_id(self, payable_id, transaction_id=None):
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

    def get_antifraud_analysis_by_id(self, analysis_id, transaction_id=None):
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