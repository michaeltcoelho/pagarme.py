# coding:utf-8
import unittest

from pagarme.resources import BankAccount


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.bank_account = {
            'bank_code': '341',
            'agencia': '0932',
            'agencia_dv': '5',
            'conta': '58054',
            'conta_dv': '1',
            'document_number': '26268738888',
            'legal_name': 'API BANK ACCOUNT'
        }

    def test_create(self):
        bank_account = BankAccount(self.bank_account)
        bank_account.create()

        self.assertEqual(bank_account.success(), True)
        self.assertEqual(bank_account.bank_code, self.bank_account['bank_code'])
        self.assertEqual(bank_account.agencia, self.bank_account['agencia'])
        self.assertEqual(bank_account.agencia_dv, self.bank_account['agencia_dv'])
        self.assertEqual(bank_account.conta, self.bank_account['conta'])
        self.assertEqual(bank_account.conta_dv, self.bank_account['conta_dv'])
        self.assertEqual(bank_account.document_number, self.bank_account['document_number'])
        self.assertEqual(bank_account.legal_name, self.bank_account['legal_name'])

    def test_find(self):
        bank_account = BankAccount.find(1714444)

        self.assertEqual(bank_account.success(), True)
        self.assertEqual(bank_account.bank_code, self.bank_account['bank_code'])
        self.assertEqual(bank_account.agencia, self.bank_account['agencia'])
        self.assertEqual(bank_account.agencia_dv, self.bank_account['agencia_dv'])
        self.assertEqual(bank_account.conta, self.bank_account['conta'])
        self.assertEqual(bank_account.conta_dv, self.bank_account['conta_dv'])
        self.assertEqual(bank_account.document_number, self.bank_account['document_number'])
        self.assertEqual(bank_account.legal_name, self.bank_account['legal_name'])

    def test_all(self):
        bank_accounts = BankAccount.all()
        bank_account = bank_accounts[0]

        self.assertEqual(bank_account.success(), True)
        self.assertEqual(bank_account.bank_code, self.bank_account['bank_code'])
        self.assertEqual(bank_account.agencia, self.bank_account['agencia'])
        self.assertEqual(bank_account.agencia_dv, self.bank_account['agencia_dv'])
        self.assertEqual(bank_account.conta, self.bank_account['conta'])
        self.assertEqual(bank_account.conta_dv, self.bank_account['conta_dv'])
        self.assertEqual(bank_account.document_number, self.bank_account['document_number'])
        self.assertEqual(bank_account.legal_name, self.bank_account['legal_name'])
