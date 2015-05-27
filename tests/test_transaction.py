# coding:utf-8
import os
import unittest

from pagarme.transaction import Transaction
from pagarme.enum import payment_methods, transaction_states


class TransactionTest(unittest.TestCase):

    def setUp(self):
        self.encryption_key = os.environ['PAGARME_ENCRYPTION_KEY']
        self.card = {
            'card_number': '4901720080344448',
            'card_holder_name': 'Usuario de Teste',
            'card_expiration_date': '1217',
            'card_cvv': '314'
        }

    def test_card_hash_key_generate(self):
        response = Transaction.generate_hash_key(self.card)
        self.assertEqual(response.success(), True)

    def test_create_without_antifraud(self):
        hash_key = Transaction.generate_hash_key(self.card)
        transaction = Transaction({
            'card_hash': hash_key.card_hash,
            'amount': 20000,
            'payment_method': payment_methods.CREDIT_CARD,
            'installments': '1',
            'capture': True,
            'postback_url': 'http://requestb.in/19by7s31'
        })
        created = transaction.create()
        self.assertEqual(created, True)

    @unittest.skip('This test must be runned only when the AntiFraud option is enabled')
    def test_create_with_antifraud(self):
        hash_key = Transaction.generate_hash_key(self.card)
        transaction = Transaction({
            'card_hash': hash_key.card_hash,
            'amount': '20000',
            'payment_method': payment_methods.CREDIT_CARD,
            'installments': '1',
            'capture': 'true',
            'postback_url': 'http://requestb.in/ysys9uys',
            'customer': {
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
            },
            'metadata': {
                'idProduto': '12345'
            }
        })
        created = transaction.create()
        self.assertEqual(created, True)
        self.assertEqual(hash_key.card_hash, transaction.card_hash)

    def test_find(self):
        transaction = Transaction.find(208650)
        self.assertEqual(transaction.success(), True)
        self.assertEqual(transaction.amount, 20000)
        self.assertEqual(transaction.payment_method, payment_methods.CREDIT_CARD)
        self.assertEqual(transaction.installments, 1)

    def test_all(self):
        transactions = Transaction.all()
        self.assertGreater(len(transactions), 0)

    def test_refund(self):
        transaction = Transaction.all()[-1:]
        transaction[0].refund()
        self.assertEqual(transaction[0].success(), True)
        self.assertEqual(transaction[0].status, 'paid')

    def test_capture(self):
        hash_key = Transaction.generate_hash_key(self.card)
        transaction = Transaction({
            'card_hash': hash_key.card_hash,
            'amount': 20000,
            'payment_method': payment_methods.CREDIT_CARD,
            'installments': '1',
            'capture': False,
            'postback_url': 'http://requestb.in/1617iyy1'
        })

        transaction.create()
        self.assertEqual(transaction.status, transaction_states.PROCESSING)

        transaction.capture()
        self.assertEqual(transaction.status, transaction_states.AUTHORIZED)

    @unittest.skip('This test must be runned only in non test environment')
    def test_capture(self):
        transaction = Transaction.all()[0]
        transaction.collect_payment()
        self.assertEqual(transaction.success(), True)

    def test_get_all_antifraud_analysis(self):
        analysis = Transaction().get_all_antifraud_analysis(211252)
        analysis_first = analysis[0]
        self.assertEqual(analysis_first.success(), True)
        self.assertEqual(analysis_first.score, 61.13)
        self.assertEqual(analysis_first.object, 'antifraud_analysis')

    def test_get_antifraud_analisys_by_id(self):
        analysis = Transaction().get_antifraud_analysis_by_id(analysis_id=431, transaction_id=211252)
        self.assertEqual(analysis.success(), True)
        self.assertEqual(analysis.score, 61.13)
        self.assertEqual(analysis.object, 'antifraud_analysis')
        self.assertEqual(analysis.status, 'approved')

    def test_calculate_installments_amount(self):
        installment = {
            'max_installments': 3,
            'free_installments': 1,
            'interest_rate': 13,
            'amount': 1300
        }
        installments = Transaction().calculate_installments_amount(installment)

        self.assertEqual(installments.success(), True)
        self.assertEqual(installments['1']['amount'], 1300)
        self.assertEqual(installments['1']['installment'], 1)
        self.assertEqual(installments['1']['installment_amount'], 1300)

        self.assertEqual(installments['2']['amount'], 1615)
        self.assertEqual(installments['2']['installment'], 2)
        self.assertEqual(installments['2']['installment_amount'], 807)

        self.assertEqual(installments['3']['amount'], 1757)
        self.assertEqual(installments['3']['installment'], 3)
        self.assertEqual(installments['3']['installment_amount'], 586)