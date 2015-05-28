# coding:utf-8
import unittest

from pagarme.resources import Recipient


class RecipientTest(unittest.TestCase):

    def setUp(self):
        self.id = 're_cia8ixe9z00dkzq6d5jd40ovh'

    def test_create(self):
        recipient = Recipient({
            'transfer_interval': 'daily',
            'transfer_day': 5,
            'bank_account': {
                'bank_code': '341',
                'agencia': '0932',
                'agencia_dv': '5',
                'conta': '58054',
                'conta_dv': '1',
                'document_number': '26268738888',
                'legal_name': 'API BANK ACCOUNT'
            }
        })
        recipient.create()
        self.assertEqual(recipient.success(), True)

    def test_balance(self):
        recipient = Recipient.find(self.id)
        balance = recipient.balance()

        self.assertEqual(balance.success(), True)
        self.assertEqual(balance.available.amount, 0)
        self.assertEqual(balance.waiting_funds.amount, 0)
        self.assertEqual(balance.transferred.amount, 0)

    def test_find(self):
        recipient = Recipient.find(self.id)

        self.assertEqual(recipient.success(), True)
        self.assertEqual(recipient.transfer_interval, 'daily')
        self.assertEqual(recipient.transfer_day, 5)
        self.assertIsNotNone(recipient.bank_account)

    def test_all(self):
        recipients = Recipient.all()
        recipient = recipients[0]
        self.assertEqual(recipient.success(), True)
        self.assertGreater(len(recipients), 0)
