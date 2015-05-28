# coding:utf-8
import unittest

from pagarme.resources.resource import Resource


class ContextTest(unittest.TestCase):
    def test_to_dict(self):
        data = {
            "amount": 31000,
            "days": 30,
            "name": "Plano Ouro",
            "trial_days": 0,
            "payment_methods": [
                "boleto",
                "credit_card"
            ],
            "test": {
                "types": [
                    "1",
                    "2"
                ]
            },
            "installments": 1
        }
        resource = Resource(attributes=data)
        self.assertDictEqual(resource.to_dict(), data)

    def test_getter(self):
        data = {
            "amount": 31000,
            "days": 30,
            "name": "Plano Ouro",
            "trial_days": 0,
            "payment_methods": [
                "boleto",
                "credit_card"
            ],
            "installments": 1
        }
        resource = Resource(data)
        self.assertEqual(resource.amount, 31000)
        self.assertEqual(resource.days, 30)
        self.assertEqual(resource.name, 'Plano Ouro')
        self.assertEqual(resource.trial_days, 0)
        self.assertItemsEqual(resource.payment_methods, ['boleto', 'credit_card'])
        self.assertEqual(resource.installments, 1)

    def test_setter(self):
        data = {
            "amount": 31000,
            "days": 30,
            "name": "Plano Ouro",
            "trial_days": 0,
            "payment_methods": [
                "boleto",
                "credit_card"
            ],
            "installments": 1
        }
        resource = Resource(data)

        self.assertEqual(resource.amount, 31000)

        resource.amount = 30000
        self.assertEqual(resource.amount, 30000)

        self.assertEqual(resource.days, 30)

        resource.days = 31
        self.assertEqual(resource.days, 31)

        self.assertEqual(resource.trial_days, 0)

        resource.trial_days = 1
        self.assertEqual(resource.trial_days, 1)

        self.assertItemsEqual(resource.payment_methods, ['boleto', 'credit_card'])

        resource.payment_methods.append('debit_card')
        self.assertItemsEqual(resource.payment_methods, ['boleto', 'credit_card', 'debit_card'])

        self.assertEqual(resource.installments, 1)

        resource.installments = 2
        self.assertEqual(resource.installments, 2)

    def test_on_success(self):
        data = {
            "amount": 31000,
            "days": 30,
            "name": "Plano Ouro",
            "trial_days": 0,
            "payment_methods": [
                "boleto",
                "credit_card"
            ],
            "test": {
                "types": [
                    "1",
                    "2"
                ]
            },
            "installments": 1
        }
        resource = Resource(attributes=data)
        self.assertEqual(resource.success(), True)

    def test_on_errors(self):
        data = {
            "errors": [{
                "type": "invalid_parameter",
                "parameter_name": "api_key",
                "message": "api_key está faltando"
            }],
            "url": "/transactions",
            "method": "get"
        }
        resource = Resource(attributes=data)
        self.assertEqual(resource.success(), False)
