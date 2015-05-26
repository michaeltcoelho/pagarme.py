# coding:utf-8
import os
import unittest

from pagarme.transaction import Transaction
from pagarme.enum import payment_method
from pagarme.metadata import MetaData, CustomerMetaData


class TransactionTest(unittest.TestCase):

    def setUp(self):
        self.encryption_key = os.environ['PAGARME_ENCRYPTION_KEY']
        self.card = {
            'card_number': 4901720080344448,
            'card_holder_name': 'Usuario de Teste',
            'card_expiration_date': 1217,
            'card_cvv': 314
        }
        self.customer = CustomerMetaData({
            'name': 'John Appleseed',
            'document_number': '92545278157',
            'email': 'jappleseed@apple.com',
            'address': {
                'street': 'Av. Brigadeiro Faria Lima',
                'complementary': '8º andar',
                'street_number': '2941',
                'zipcode': '01452000',
                'neighborhood': 'Jardim Paulistano'
            },
            'phone': {
                'ddd': '11',
                'number': '30713261'
            }
        })
        self.metadata = MetaData({
            'idProduto': 12345
        })

    def test_card_hash_key_generate(self):
        response = Transaction.generate_hash_key(self.card)
        self.assertEqual(response.success(), True)

    @unittest.skip('skipped')
    def test_create_without_metadata_and_customer(self):
        card_hash = Transaction.generate_hash_key(self.card)
        transaction = Transaction({
            'card_hash': card_hash.card_hash,
            'amount': 20000,
            'payment_method': payment_method.CREDIT_CARD,
            'installments': '1',
            'capture': True,
            'postback_url': 'http://requestb.in/19by7s31'
        })
        created = transaction.create()
        self.assertEqual(created, True)

    def test_create_with_metadata_and_customer(self):
        card_hash = Transaction.generate_hash_key(self.card)
        transaction = Transaction({
            'card_hash': card_hash.card_hash,
            'amount': 20000,
            'payment_method': payment_method.CREDIT_CARD,
            'installments': '1',
            'capture': True,
            'postback_url': 'http://requestb.in/19by7s31'
        })
        created = transaction.create(metadata=self.metadata, customer=self.customer)
        self.assertEqual(created, True)